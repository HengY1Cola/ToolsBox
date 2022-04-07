import json
import datetime
import requests
import time
from urllib.parse import urlencode


# Warning ⚠️
# 注意：反复登陆会导致需要验证码
# 这时候用浏览器打开对应的网站登陆一次就好了

class GetMid:
	def __init__(self, acc: str, password: str):
		self.acc = acc
		self.password = password
		self.session = None
		self.sunNum = 999

	def __login(self):
		nowTime = int(round(time.time() * 1000))
		data = {
			"userName": self.acc,
			"password": self.password,
			"loginValidCode": "",
			"_": nowTime
		}
		url = "https://tuanapi.12355.net/login/adminLogin?" + urlencode(data)
		s = requests.session()
		r = s.get(url)
		if r.json()['status'] != "OK":
			raise Exception(str(r.text))
		self.session = s

	def __getSunNum(self):
		# todo 获得oid
		nowTime = int(round(time.time() * 1000))
		url = "https://tuanapi.12355.net/login/getSessionAccount?_=" + str(nowTime)
		oid = self.session.get(url).json()['account']['oid']
		# todo 获得人数
		today = datetime.datetime.today()
		year = today.year
		month = '{:02d}'.format(today.month)
		yearMonth = str(year) + month
		data = {
			"curPage": 1,
			"pageSize": 1,
			"yearMonth": yearMonth,
			"oid": oid,
			"_": nowTime
		}
		header = {
			"authorize_name": str(oid)
		}
		url = "https://tuanapi.12355.net/api/bg/organizationStatistics/getOrgStatisticsLists?" + urlencode(data)
		r = self.session.get(url, headers=header)
		self.sunNum = r.json()['data']['OrgList'][0]['sumLeagueMember']

	def __getIdList(self):
		# todo 获取mid
		url = "https://tuanapi.12355.net/api/v1/admin/members/page"
		data = {
			"page": 1,
			"pageSize": int(self.sunNum)
		}
		header = {
			"Content-Type": "application/json",
			"Accept": "application/json, text/javascript, */*; q=0.01",
			"Origin": "https://tuan.12355.net",
			"Referer": "https://tuan.12355.net/",
			"Host": "tuanapi.12355.net",
			"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
						  "Chrome/99.0.4844.83 Safari/537.36",
		}
		r = self.session.post(url, data=json.dumps(data), headers=header).json()
		listData = r['listData']
		midList = [each['mid'] for each in listData]
		return midList

	def run(self) -> list:
		try:
			self.__login()
			self.__getSunNum()
			return self.__getIdList()
		except Exception as e:
			print(f"获得错误：{str(e)}")


if __name__ == "__main__":
	account, password = "", ""
	session = GetMid(account, password)
	idList = session.run()
	print(idList)

