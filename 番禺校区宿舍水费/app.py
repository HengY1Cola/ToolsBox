import json
import re
import time
from Crypto.Cipher import AES
import base64
import requests

ROOT_DOMAIN = "http://10.136.2.5/IBSjnuweb/"


class IBSService:
    def __init__(self, acc: str):
        if acc == "":
            raise Exception("账号不能为空")
        self.key = "CetSoftEEMSysWeb"
        self.iv = b"\x19\x34\x57\x72\x90\xAB\xCD\xEF\x12\x64\x14\x78\x90\xAC\xAE\x45"
        self.__check(acc)
        self.__checkOnline()

    @staticmethod
    def getIBSClient() -> requests.Session:
        s = requests.Session()
        header = {
            "Content-Type": "application/json; charset=UTF-8",
            'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/91.0.4472.77 Safari/537.36",
            "X-Forwarded-For": '127.0.0.1',
        }
        s.headers.update(header)
        return s

    @staticmethod
    def __checkOnline():
        try:
            requests.get(ROOT_DOMAIN, timeout=3)
        except requests.exceptions.ConnectTimeout:
            raise Exception("超时链接，请使用校园网/内网穿透")

    def __getEncrypt(self, text) -> str:
        text = text.replace(" ", "")  # 这里是个大坑
        text = text.replace("|", " ")  # 为了绕过中间的空格进入加密
        BS = 16
        pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
        text = pad(text)
        o_aes = AES.new(self.key.encode(), AES.MODE_CBC, self.iv)
        esb = o_aes.encrypt(text.encode("UTF8"))
        return base64.b64encode(esb).decode("UTF8")

    def __check(self, acc):
        re_right = re.compile(r'^T(\d{5,6})$')
        if not re_right.match(acc):
            raise Exception("宿舍号不符合规则")
        self.acc = acc

    def __generateToken(self):
        timeArray = time.localtime(time.time())
        token_time = time.strftime("%Y-%m-%d | %H:%M:%S", timeArray)
        arr = {
            'userID': self.customerId,
            'tokenTime': token_time,
        }
        return self.__getEncrypt(json.dumps(arr))

    def __getIBSRequestHeader(self):
        timeArray = time.localtime(time.time())
        DateTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        Header = {
            "Token": self.__generateToken(),
            'DateTime': DateTime,
        }
        return Header

    def __login(self, paw):
        self.session = self.getIBSClient()
        postUrl = ROOT_DOMAIN + "WebService/JNUService.asmx/Login"
        postData = {"password": paw, "user": self.acc}
        responseRes = self.session.post(postUrl, json=postData)
        response = json.loads(responseRes.text)
        customerId = response['d']['ResultList'][0]['customerId']
        if customerId == 0:
            raise Exception("未能找到该宿舍")
        self.customerId = customerId

    def __getUserInfo(self):
        center_url = ROOT_DOMAIN + "WebService/JNUService.asmx/GetUserInfo"
        header = self.__getIBSRequestHeader()
        responseRes = self.session.post(center_url, headers=header)
        self.response = responseRes.text

    def __parseTxt(self):
        roomInfo = json.loads(self.response)['d']['ResultList'][0]['roomInfo']
        allowanceInfo = json.loads(self.response)['d']['ResultList'][0]['allowanceInfo']
        resultInfo = {
            'balance': roomInfo[1]['keyValue'],
            'subsidies': allowanceInfo[0]['keyValue'],
        }
        return resultInfo

    def run(self):
        try:
            paw = self.__getEncrypt(self.acc)
            self.__login(paw)  # 进行登陆
            self.__getUserInfo()  # 拿到信息
            res = self.__parseTxt()  # 分析结果
            print(res)
        except Exception as e:
            print("发生错误", e)


if __name__ == '__main__':
    print("[*] 更多信息在：https://github.com/HengY1Sky/Jnu-ToolsBox 作者：HengY1")
    print("[*] ROOT_DOMAIN为学校官网，但是只能校内访问")
    print("[*] 若要提供公网访问则需要进行内网穿透～")
    print("[*] 更多接口只需要更换对应的路径即可然后解析内容 ✧(≖ ◡ ≖✿)")
    IBSService("T110222").run()
