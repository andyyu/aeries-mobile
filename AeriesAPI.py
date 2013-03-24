from requests import session
import unicodedata
from bs4 import BeautifulSoup
class AeriesAPI:

	def __init__(self,username,password):
		self.user=username
		self.pw=password
		self.login()
	def login(self):
		payload = {
		    'UserName': self.user,
		    'Password': self.pw
		}

		self.session=session()
		with self.session as s:
		    s.post('https://mystudent.fjuhsd.net/loginprochome.asp', data=payload)		
		self.gradebookHTML= self.__getPageHTML('https://mystudent.fjuhsd.net/GradebookSummary.asp')

	def getPeriods(self):
		soup = BeautifulSoup(self.gradebookHTML)
		periods = []
		rows = soup.find_all("tr", "NormalClickableRowEven")
		odds=soup.find_all("tr","NormalClickableRow")
		for i in odds:
			rows.append(i)
		rows=[row for row in rows if row.contents[9].text.encode('ascii','ignore')==""] #get rid of past terms			
		for period in rows:
			classinfo = {}
			classinfo["name"] = (period.contents[1].text.encode('ascii','ignore'))
			classinfo["num"] = int(period.contents[3].text.encode('ascii','ignore'))
			classinfo["percentgrade"] = (period.contents[5].text.encode('ascii','ignore'))
			classinfo["lettergrade"] = (period.contents[6].text.encode('ascii','ignore'))
			classinfo["missingassign"] = (period.contents[7].text.encode('ascii','ignore'))
			#some stuff i'm working on with the links
			link= period.contents[1].contents[0].get('href').split('&GrdBk=')
			classinfo["class_id"] = link[1].encode('ascii','ignore')		
			self.base_period_url = ("https://mystudent.fjuhsd.net/"+link[0]+"&GrdBk=").encode('ascii','ignore')
			classinfo["full_url"]=period.contents[1].contents[0].get('href').encode('ascii','ignore')
			periods.append(classinfo)
		periods=sorted(periods, key=lambda period: period["num"]) #sort them by period numbers
		return periods


	def getPeriodAssignments(url):
		html=self.__getPageHTML(url)
		soup=BeautifulSoup(html)

	def __getPageHTML(self,url):
		with self.session as s:
			request = s.get(url)
			string=request.text.encode('ascii','ignore')
			return string

