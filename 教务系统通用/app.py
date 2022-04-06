import urllib.parse
from requests import cookies
import execjs
from bs4 import BeautifulSoup
import time
import urllib.parse
import requests


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


def getScheduleHeader():
    headers = {
        "authority": "jw.jnu.edu.cn",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,"
                  "image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-language": "zh-CN,zh;q=0.9",
        "referer": "https://jw.jnu.edu.cn/new/index.html",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/100.0.4896.60 Safari/537.36"
    }
    return headers


class LoginScript:
    def __init__(self, acc: str, paw: str):
        self.jwUrl = "https://icas.jnu.edu.cn/cas/login?service=" \
                     "https%3A%2F%2Fauth5.jnu.edu.cn%2Frump_frontend%2FloginFromCas%2F"
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


class GetSchedule:
    def __init__(self, session: requests.Session):
        self.json = None
        self.session = session
        self.scheduleId = 4770397878132218  # 为课表的ID

    def ImitateJump(self, way: int, fromWhere: str):
        try:
            if way == 1:
                r = self.session.post(url=fromWhere, headers=getScheduleHeader(), allow_redirects=False)
            else:
                r = self.session.get(url=fromWhere, headers=getScheduleHeader(), allow_redirects=False)
            header = r.headers
            if 'Location' in header.keys():
                return header['Location']
            else:
                return ""
        except Exception as e:
            print(f"[*] form {fromWhere} Error: {e}")
            return ""

    def __getSessionToken(self):
        # todo 为了Token
        url = "https://jw.jnu.edu.cn//amp-auth-adapter/login?" \
              "service=http%3A%2F%2Fjw.jnu.edu.cn%2Flogin%3Fservice%3Dhttps%3A%2F%2Fjw.jnu.edu.cn%2Fnew%2Findex.html"
        url = self.ImitateJump(0, url)  # 拿到跳转的sessionToken
        query = dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(url).query))
        aim = query['service']  # 因为是跳转 拿到后面的
        query = dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(aim).query))  # 再次分析
        jar = requests.cookies.RequestsCookieJar()
        jar.set("own-token", query['sessionToken'])
        self.session.cookies.update(jar)

    def __getJsID(self):
        # todo 为了拿到_WEN有效
        nowTime = int(round(time.time() * 1000))
        url = "https://jw.jnu.edu.cn/jsonp/serviceCenterData.json?containLabels=true&searchKey=&_=" + str(nowTime)
        self.session.get(url, headers=getScheduleHeader())

    def __getRealTicket(self):
        # todo 为了拿到通行证
        cookie = self.session.cookies.get_dict()
        url = "https://icas.jnu.edu.cn/cas/login?" \
              "service=http%3A%2F%2Fjw.jnu.edu.cn%2Famp-auth-adapter%2FloginSuccess%3FsessionToken%3D" + cookie[
                  'own-token']
        # 以下不写循环 仅仅是为了注释每一步
        url = self.ImitateJump(0, url)
        url = self.ImitateJump(0, url)  # 这里是一块跳板
        url = self.ImitateJump(0, url)  # 这里成功拿到真正的ticket并且存入新的CASTGC
        url = self.ImitateJump(0, url, )  # 这里为301永久定向也是跳板
        self.ImitateJump(0, url)  # 成功把MOD_AMP_AUTH存入

    def __getWENCookie(self):
        # todo 拿到最后一个cookie
        # todo 先拿到gid跳转链接
        url = "https://jw.jnu.edu.cn/appShow?appId=" + str(self.scheduleId)
        url = self.ImitateJump(0, url)
        self.session.get(url, headers=getScheduleHeader())

    def __getSchedule(self):
        cookieDict = self.session.cookies.get_dict()
        # todo 拿到课表
        headers = {
            "authority": "jw.jnu.edu.cn",
            "accept": "application/json, text/javascript, */*; q=0.01",
            "accept-language": "zh-CN,zh;q=0.9",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "origin": "https://jw.jnu.edu.cn",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/100.0.4896.60 Safari/537.36",
            "x-requested-with": "XMLHttpRequest"
        }
        cookie = {
            "_WEU": cookieDict['_WEU'],
            "client_vpn_ticket": cookieDict['client_vpn_ticket'],
            "MOD_AMP_AUTH": cookieDict['MOD_AMP_AUTH'],
        }
        url = "https://jw.jnu.edu.cn/jwapp/sys/wdkb/modules/xskcb/xskcb.do"
        data = {
            "XNXQDM": "2021-2022-2"
        }
        response = requests.post(url, headers=headers, data=data, cookies=cookie)
        self.json = response.json()

    def __parseJson(self):
        info = self.json['datas']['xskcb']
        total = info['totalSize']
        print(f'[*] 查询到数量：{total}')
        rows = info['rows']
        dicFunc = lambda x: (x['KKDWDM_DISPLAY'], x['SKJS'], x['XXXQDM_DISPLAY'], x['YPSJDD'])
        res = [dicFunc(each) for each in rows]
        for each in res:
            college, teacher, where, detail = each
            print(f'[*] 来自{college} 老师：{teacher}, 校区：{where}, 细节：{detail}')

    def run(self):
        try:
            self.__getSessionToken()
            self.__getJsID()
            self.__getRealTicket()
            self.__getWENCookie()
            self.__getSchedule()
            self.__parseJson()
        except Exception as e:
            print(f"[*] 错误：{e}")


if __name__ == "__main__":
    print("[*] 更多信息：https://github.com/HengY1Sky/Jnu-ToolsBox")
    print("[*] 连续多次错误将会导致校园网被锁")
    print("[*] scheduleId换成别的后都是一个道理拿到对应的cookie就可以请求接口了")
    print("[*] 因为有多次跳转可能部分时候会失效 \n[*] 重试即可")
    account, password = "", ""
    s = LoginScript(account, password).login()
    schedule = GetSchedule(s)
    schedule.run()
