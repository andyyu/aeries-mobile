from requests import session
import unicodedata
from bs4 import BeautifulSoup
"""

"""
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


	def getPeriodAssignments(self,url):
		html=self.__getPageHTML(url)
		soup=BeautifulSoup(html)
		assignments = []
		rows = soup.find_all("tr", "NormalRowEven")
		odds=soup.find_all("tr", "NormalRow")
		realrows = []
		for i in odds:
			rows.append(i)
		for anyrow in rows:
			if anyrow.contents[1].text.encode('ascii','ignore')!="...":
				realrows.append(anyrow)
		# rows=[anyrow for anyrow in rows if anyrow.contents[1].text.encode('ascii','ignore')!="..."]
		#basically it's like
		#NormalRowEven (id: Row2 let's say)
		#--NormalRowEven (id: Row2b)
		#----NormalRowEven (id: Row2d)
		#----NormalRowEven (id: Row2f)
		#
		#so above, when you removed the one with the blank first cell, it only removed the row with the id: Row2b. Basically, 
		#look through the documentation and try to find a way to also remove all the children elements of Row2b.
		for assignment in realrows:
			assignmentinfo = {}
			assignmentinfo["name"] = (assignment.contents[1].text.encode('ascii','ignore'))
			assignmentinfo["type"] = (assignment.contents[2].text.encode('ascii','ignore'))
			assignmentinfo["score"] = int(assignment.contents[4].text.encode('ascii','ignore'))
			assignmentinfo["maxscore"] = int(assignment.contents[5].text.encode('ascii','ignore'))
			assignmentinfo["percent"] = float(assignmentinfo["score"]/assignmentinfo["maxscore"])*100
			assignments.append(assignmentinfo)
		return assignments


	def __getPageHTML(self,url):
		with self.session as s:
			request = s.get(url)
			string=request.text.encode('ascii','ignore')
			return string

