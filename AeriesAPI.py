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
		rows.append(soup.find_all("tr","NormalClickableRow"))
		for anyrow in rows:
			if anyrow.contents[9].contents[0]!=null:
				rows.remove(anyrow)
		for period in rows:
			classinfo = {}
			classinfo["name"] = (period.contents[1].text.encode('ascii','ignore'))
			classinfo["percentgrade"] = (period.contents[5].text.encode('ascii','ignore'))
			classinfo["lettergrade"] = (period.contents[6].text.encode('ascii','ignore'))
			classinfo["missingassign"] = (period.contents[7].text.encode('ascii','ignore'))
			periods.append(classinfo)
		return periods

	def getPeriodAssignments(url):
		html=self.__getPageHTML(url)
		soup=BeautifulSoup(html)
		assignments = []
		rows = soup.find_all("tr", "NormalClickableRowEven")
		rows.append(soup.find_all("tr", "NormalClickableRow"))
		for anyrow in rows:
			if anyrow.contents[0].text==null:
				rows.remove(anyrow)
		for assignment in rows:
			assignmentsoup = BeautifulSoup(assignment)
			assignmentinfo = {}
			assignmentinfo["name"] = (assignment.contents[1].text.encode('ascii','ignore'))
			assignmentinfo["type"] = (assignment.contents[2].text.encode('ascii','ignore'))
			assignmentinfo["score"] = assignmentsoup('td').elements[4]('input')[0]['value']
			assignmentinfo["maxscore"] = assignmentsoup('td').elements[5]('div')[0].text
			assignmentinfo["percent"] = (score/maxscore)*100
			assignments.append(assignmentinfo)
		return assignments


	def __getPageHTML(self,url):
		with self.session as s:
			request = s.get(url)
			string=request.text.encode('ascii','ignore')
			return string
