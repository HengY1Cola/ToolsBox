import threading
from getId import GetMid
import requests
import urllib.parse
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor
from collections import Counter

# 有啥问题直接开ISSUE即可
# 项目地址：https://github.com/HengY1Sky/Jnu-ToolsBox

def makeHeader(host, origin, referer):
    headers = {
        'Host': host,
        'Origin': origin,
        'Referer': referer,
        'X-Litemall-Token': '',
        'X-Litemall-IdentiFication': 'young',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/51.0.2704.103 Safari/537.36',
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-Requested-With': 'com.tencent.mm',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    return headers


class AppMain:
    def __init__(self, acc: str, pas: str):
        self.lock = threading.RLock()
        self.acc = acc
        self.pas = pas
        self.idList = None
        self.failList = []
        self.success = 0
        self.errList = []
        self.lock = threading.Lock()

    @staticmethod
    def getSign(mid):
        url = "https://tuanapi.12355.net/questionnaire/getYouthLearningUrl?mid=" + str(mid)
        response = requests.get(url, headers=makeHeader('tuanapi.12355.net',
                                                        'https://tuan.12355.net',
                                                        'https://tuan.12355.net/wechat/view/YouthLearning/page.html'))
        resJson = response.json()
        signUrl = resJson['youthLearningUrl']
        sign = signUrl.split('?')
        return sign[1][5:]

    @staticmethod
    def getToken(sign):
        payload = "sign=" + urllib.parse.quote(sign)
        url = "https://youthstudy.12355.net/apih5/api/user/get"
        response = requests.post(url, headers=makeHeader('youthstudy.12355.net',
                                                         'https://youthstudy.12355.net',
                                                         'https://youthstudy.12355.net/h5/'), data=payload)
        resJson = response.json()
        return resJson["data"]["entity"]["token"]

    @staticmethod
    def getChapterId():
        url = "https://youthstudy.12355.net/apih5/api/young/chapter/new"
        headers = {
            'X-Litemall-IdentiFication': 'young'
        }
        response = requests.get(url, headers=headers)
        j = response.json()
        return j["data"]["entity"]["id"]

    @staticmethod
    def finalDone(token, cid):
        headers = makeHeader('youthstudy.12355.net', 'https://youthstudy.12355.net', 'https://youthstudy.12355.net/h5/')
        headers["X-Litemall-Token"] = token
        url = "https://youthstudy.12355.net/apih5/api/young/course/chapter/saveHistory"
        payload = "chapterId=" + str(cid)
        response = requests.post(url, headers=headers, data=payload)
        j = response.json()
        return j

    def factory(self, mid: int) -> (bool, int):
        try:
            cid = self.getChapterId()
            sign = self.getSign(mid)
            token = self.getToken(sign)
            res = self.finalDone(token, cid)
            if res["errno"] == 0:
                return True, 0
            else:
                self.lock.acquire()
                self.errList.append(res['errmsg'])
                self.lock.release()
                return False, mid
        except Exception as e:
            self.lock.acquire()
            self.errList.append(str(e))
            self.lock.release()
            print(f"[*] mid为：{mid}发生错误：{e}")
            return False, mid

    def __initList(self):
        try:
            self.idList = GetMid(self.acc, self.pas).run()
        except Exception as e:
            print(f"initList 发生错误：{e}")
            exit()

    def __doMission(self):
        # todo 判断数量
        if len(self.idList) == 0:
            print(f"[*] initList 数量为0")
            exit()
        # todo 多线程执行
        with tqdm(total=len(self.idList)) as pbar:
            pbar.set_description('Processing:')
            executor = ThreadPoolExecutor(max_workers=2)
            for data in executor.map(self.factory, self.idList):
                pbar.update(1)
                flag, mid = data
                if not flag:
                    self.failList.append(mid)
                else:
                    self.success += 1
        # todo 显示错误原因以及次数
        result = Counter(self.errList)
        print("[*] " + str(result))
        # todo 再次执行错误名单
        if self.failList:
            print("[*] 存在错误名单，开始修复")
            temp = []
            with tqdm(total=len(self.failList)) as pbar:
                pbar.set_description('Fixing:')
                for each in self.failList:
                    flag, _ = self.factory(each)
                    pbar.update(1)
                    if not flag:
                        temp.append(each)
                    else:
                        self.success += 1
            self.failList = temp
        # todo 处理结果
        rate = round(self.success / len(self.idList), 2) * 100
        print(f"[*] 总人数：{len(self.idList)} 成功为：{self.success} 学习完成率为：{rate}")
        print(f"[*] 失败人数：{len(self.failList)} 为{str(self.failList)}")
        print("[*] 任务完成")

    def run(self):
        self.__initList()
        self.__doMission()


if __name__ == "__main__":
    print("更多信息请到：https://github.com/HengY1Sky/Jnu-ToolsBox")
    account, password = "", ""
    newOne = AppMain(account, password)
    newOne.run()