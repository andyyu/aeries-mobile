from requests import session
import unicodedata
from bs4 import BeautifulSoup
"""

"""
class AeriesAPI:

	def __init__(self,username,password):
		self.user=username
		self.pw=password
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


	def getPeriodAssignments(self,id):
		url="https://mystudent.fjuhsd.net/GradebookStuScores.asp?cache=3%2F28%2F2013+11%3A49%3A05+PM&GrdBk="+id
		html=self.__getPageHTML(url)
		soup=BeautifulSoup(html)
		assignments = []
		rows = soup.find_all("tr", "NormalRowEven")
		odds=soup.find_all("tr", "NormalRow")
		for i in odds:
			rows.append(i)
		#get all rows from soup
		totalscores = [anyrow for anyrow in rows if anyrow.find("td", {"align": "center"}) = None]
		for score in totalscores:
			scoreinfo = {}
			scoreinfo["name"] = (score.contents[0].text.encode('ascii','ignore'))
			score = score.contents[1].text.encode('ascii','ignore')
			scoreinfo["score"] = 0 if score=="[]" or isinstance (score, int) else int(score)
			scoreinfo["maxscore"] = int(score.contents[2].text.encode('ascii','ignore'))
			scoreinfo["percent"] = int(score.contents[3].text.encode('ascii','ignore'))
		rows=[anyrow for anyrow in rows if (anyrow.find("td", {"align" : "center"})!= None  and anyrow.contents[0].text.encode('ascii','ignore').isdigit())]
		#gets the total / cumulative grades
		for assignment in rows:
			assignmentinfo = {}
			assignmentinfo["name"] = (assignment.contents[1].text.encode('ascii','ignore'))
			assignmentinfo["type"] = (assignment.contents[2].text.encode('ascii','ignore'))
			score=assignment.contents[4].text.encode('ascii','ignore')
			assignmentinfo["score"] = 0 if score=="[]" or isinstance (score, int) else int(score)
			assignmentinfo["maxscore"] = int(assignment.contents[5].text.encode('ascii','ignore'))
			assignmentinfo["missing"] = true if score =="[]" else false
			if assignmentinfo["maxscore"] != 0:
				assignmentinfo["percent"] = ('%.2f' % ((float (assignmentinfo["score"])/ float (assignmentinfo["maxscore"]))*100)) + "%"
			else:
				assignmentinfo["percent"] = "100%"
			assignments.append(assignmentinfo)
		assignments=sorted(assignments, key=lambda assignment: assignment["name"])
		#gets the individual assignments
		return {["totalscores"] = scoreinfo : ["assignments"] = assignments}

	

	def __getPageHTML(self,url):
		with self.session as s:
			request = s.get(url)
			string=request.text.encode('ascii','ignore')
			return string

