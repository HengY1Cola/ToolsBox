import json
import os
import random
import time
import urllib.parse
from requests import cookies
import execjs
from bs4 import BeautifulSoup
import urllib.parse
import requests

STEP = {
    0: "7f6d456b-2372-4b80-8e5a-0f6bf8c979c4",
    1: "c26f7e15-3fd6-4fcc-a2ee-2d72ec4dc725",
    2: "3d45bec2-f8b8-48a6-a168-868db11b43c0",
    3: "a529aa60-4246-4a33-9879-04f5ec6951e2",
    4: "20105737-bde6-4e0a-8c2f-f4f07e0016e8",
    5: "8f5e0400-e582-41be-afaa-3810faf3ef99",
}


def getHeader():
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:98.0) Gecko/20100101 Firefox/98.0",
        "Host": "icas.jnu.edu.cn",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Origin": "https://icas.jnu.edu.cn",
        "Referer": "https://icas.jnu.edu.cn/cas/login?service=https://info.jnu.edu.cn/",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    return header


def getLibHeader():
    header = {
        "Host": "libtrain.jnu.edu.cn",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:99.0) Gecko/20100101 Firefox/99.0",
        "Referer": "https://libtrain.jnu.edu.cn/Web/User"
    }
    return header


class LoginScript:
    def __init__(self, acc: str, paw: str):
        self.jwUrl = "https://icas.jnu.edu.cn/cas/login?service=https://libtrain.jnu.edu.cn/api/index/login"
        self.paw, self.acc = None, None
        self.__check(acc, paw)
        self.lt = None
        self.execution = None
        try:
            self.__parse()
            self.rsa = None
            self.___getDes()
        except Exception as e:
            print(f"[*] 初始化工作错误：{e}")

    def ___getDes(self):
        with open('des.js', 'r', encoding='UTF-8') as f:
            js_code = f.read()
        data = self.acc + self.paw + self.lt
        firstKey, secondKey, thirdKey = "1", "2", "3"
        self.rsa = execjs.compile(js_code).call("strEnc", data, firstKey, secondKey, thirdKey)

    def __check(self, acc, paw):
        if acc == "" or paw == "":
            raise Exception("账号/密码不能为空")
        self.acc = acc
        self.paw = paw

    def __parse(self):
        url = "https://icas.jnu.edu.cn/cas/login"
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml')
        self.lt = soup.select('#lt')[0].attrs['value']
        self.execution = soup.select('#loginForm > input[type=hidden]:nth-child(9)')[0].attrs['value']

    def __getSession(self):
        # todo 拿到session 此处的session只能使用一次
        header = getHeader()
        temp = requests.session()
        temp.get(url=self.jwUrl, headers=header, allow_redirects=False)
        cookie = temp.cookies.get_dict()
        lastSession = cookie['JSESSIONID']
        # todo 拿到对应的跳转链接
        sessions = requests.session()
        data = {
            "rsa": self.rsa,
            "ul": len(self.acc),
            "pl": len(self.paw),
            "lt": self.lt,
            "execution": self.execution,
            "_eventId": "submit"
        }
        cookie = {
            "JSESSIONID": lastSession,
        }
        r = sessions.post(url=self.jwUrl, headers=header, data=data, allow_redirects=False, cookies=cookie)
        header = r.headers
        # todo 拿到通行证
        if 'Location' in header.keys():
            location = header['Location']
            query = dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(location).query))
            jar = requests.cookies.RequestsCookieJar()
            jar.set("own-ticket", query['ticket'])
            sessions.cookies.update(jar)
            sessions.get(url=location, headers=header, allow_redirects=False)
            return sessions
        else:
            raise Exception("账号密码错误 \n 多次错误将会导致账号被锁")

    def login(self) -> requests.Session:
        return self.__getSession()


class GetRootPass:
    def __init__(self, acc: str, paw: str):
        self.__ping()  # 检查网络
        self.json = None
        self.__loadJson()  # 加载答案库
        self.acc = None
        self.paw = None
        self.session = None
        self.__checkAndLogin(acc, paw)  # 检查账号是否正确
        self.step = 0
        self.stepUrl = None
        self.examId = None
        self.questionList = None

    @staticmethod
    def __ping():
        try:
            requests.get("https://libtrain.jnu.edu.cn/")
            print("[*] 校园网通畅～")
        except Exception as e:
            raise Exception("请在校园网内操作～")

    def __loadJson(self):
        try:
            filePath = os.path.dirname(__file__)
            jsonPath = os.path.join(filePath, 'QA.json')
            with open(jsonPath, 'r') as load_f:
                self.json = json.load(load_f)
            print("[*] 答案库加载完毕")
        except Exception as e:
            raise e

    def __checkAndLogin(self, acc: str, paw: str):
        if acc == "" or paw == "":
            raise Exception("账号密码不能为空")
        try:
            self.session = LoginScript(acc, paw).login()
            self.acc, self.paw = acc, paw
            print("[*] 账号密码验证成功")
        except Exception as e:
            raise e

    def __getUid(self):
        aimUrl = "https://libtrain.jnu.edu.cn/web/User/cblogin?userid=" + self.acc + "&shcool=jndx"
        self.session.get(aimUrl, headers=getLibHeader(), allow_redirects=False)

    def __getJumpUrl(self):
        # todo 拿到跳转链接
        try:
            aimUrl = "https://libtrain.jnu.edu.cn/Web/User"
            jar = requests.cookies.RequestsCookieJar()
            jar.set("from", "0")
            self.session.cookies.update(jar)
            r = self.session.get(aimUrl, headers=getLibHeader())
            soup = BeautifulSoup(r.text, 'lxml')
            self.stepUrl = soup.select(".operatelist")[0].contents[1].attrs['href']
            self.__getUid()
        except Exception as e:
            raise Exception(f"getJumpUrl错误 {e}")

    def __judgeStep(self):
        try:
            aimUrl = "https://libtrain.jnu.edu.cn/Web/Exam?cid=" + STEP[self.step]
            r = self.session.get(aimUrl, headers=getLibHeader(), allow_redirects=False)
            while 'Location' in r.headers:
                self.step += 1
                if self.step == 6:
                    break
                aimUrl = "https://libtrain.jnu.edu.cn/Web/Exam?cid=" + STEP[self.step]
                time.sleep(0.5)
                r = self.session.get(aimUrl, headers=getLibHeader(), allow_redirects=False)
            current = {
                0: "初中生", 1: "高中生", 2: "大学生", 3: "研究生", 4: "博士生", 5: "博士后", 6: "答题完毕",
            }
            print(f'[*] 当前的步骤为{current[self.step]}')
            if self.step == 6:
                print("[*] 答题退出")
                exit(0)
            jar = requests.cookies.RequestsCookieJar()
            jar.set("real-cid", STEP[self.step])
            self.session.cookies.update(jar)
        except Exception as e:
            raise Exception(f"judgeStep 发生错误：{e}")

    def __getStart(self):
        try:
            # todo 只要请求一次就是开启了新的了
            aimUrl = "https://libtrain.jnu.edu.cn/Web/Exam?cid=" + self.session.cookies.get_dict()['real-cid']
            r = self.session.get(aimUrl, headers=getLibHeader())
            soup = BeautifulSoup(r.text, 'lxml')
            self.examId = soup.select("#examRecordDetailsId")[0].attrs['value']  # 本次答题的编号
            self.questionList = soup.select("#stIds")[0].attrs['value'].split(",")  # 本次题号
        except Exception as e:
            raise Exception(f"getStart 发生错误：{e}")

    def __ifCorrect(self):
        try:
            aimUrl = "https://libtrain.jnu.edu.cn/web/exam/GetGameRole"
            spend = str(random.randint(8, 32))
            data = {
                "zid": self.session.cookies.get_dict()['real-cid'],
                "examRecordDetailsId": self.examId,
                "spendtime": spend,
            }
            r = self.session.post(aimUrl, data=data, headers=getLibHeader()).json()
            print(f"[*] 当前阶段 {r['Msg']}")
        except Exception as e:
            raise Exception(f"ifCorrect 发生错误：{e}")

    def __getAns(self):
        try:
            aimUrl = "https://libtrain.jnu.edu.cn/web/Exam/GetAnswer"
            total = 0
            for each in self.questionList:  # 一道道题来做
                flag = False
                ans, spend = None, str(random.randint(8, 32))  # 处理每一道题的答案/耗时
                for eachAns in self.json:
                    if eachAns['question'] == each:  # 如果找得到
                        ans = str(eachAns['answer']).replace(",", "%2C")
                        data = {
                            "stid": each,
                            "answer": ans,
                            "zid": self.session.cookies.get_dict()['real-cid'],
                            "examRecordDetailsId": self.examId,
                            "spendtime": spend,
                            "helpId": "00000000-0000-0000-0000-000000000000"
                        }
                        self.session.post(aimUrl, data=data).json()
                        total += 1
                        flag = True
                        break
                if flag:  # 如果为真则这道题搞定了
                    continue
                else:  # 添加进入题库
                    data = {
                        "stid": each,
                        "answer": "6c9148c6-6841-4c01-8bc6-1e350b0c0daf",  # 随便搪塞一个
                        "zid": self.session.cookies.get_dict()['real-cid'],
                        "examRecordDetailsId": self.examId,
                        "spendtime": spend,
                        "helpId": "00000000-0000-0000-0000-000000000000"
                    }
                    r = self.session.post(aimUrl, data=data, headers=getLibHeader()).json()
                    ans = r['examQuestion']['answer']
                    self.json.append({"question": each, "answer": ans})
            if total == len(self.questionList):
                self.__ifCorrect()
            else:
                print("[*] 已经更新题库，开始新的一轮答题")
        except Exception as e:
            raise Exception(f"getAns 发生错误：{e}")

    def run(self):
        times = 0
        while self.step < 6:
            if times >= 9:
                raise Exception("尝试过多次数")
            times += 1
            self.__getJumpUrl()
            try:
                self.__judgeStep()
                self.__getStart()
                self.__getAns()
            except Exception as e:
                print(f"发生错误 {e}")


if __name__ == "__main__":
    account, password = "", ""
    GetRootPass(account, password).run()
