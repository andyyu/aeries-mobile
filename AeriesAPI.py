# coding=utf-8
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
		soup=BeautifulSoup(self.gradebookHTML)
		images=soup.find_all(src='images/btnLogin.gif')
		if len(images)>0:
			raise Exception("Incorrect Username or Password!")

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
			classinfo["name"] = (period.contents[1].text)
			classinfo["num"] = int(period.contents[3].text)
			classinfo["percentgrade"] = (period.contents[5].text)
			classinfo["lettergrade"] = (period.contents[6].text)
			classinfo["missingassign"] = (period.contents[7].text)
			#some stuff i'm working on with the links
			link= period.contents[1].contents[0].get('href').split('&GrdBk=')
			classinfo["class_id"] = link[1].encode('ascii','ignore')		
			self.base_period_url = ("https://mystudent.fjuhsd.net/"+link[0]+"&GrdBk=").encode('ascii','ignore')
			classinfo["full_url"]=period.contents[1].contents[0].get('href')
			periods.append(classinfo)
		periods=sorted(periods, key=lambda period: period["num"]) #sort them by period numbers
		return periods


	def getPeriodAssignments(self,id):
		url="https://mystudent.fjuhsd.net/GradebookStuScores.asp?cache=3%2F28%2F2013+11%3A49%3A05+PM&GrdBk="+id
		html=self.__getPageHTML(url)
		soup=BeautifulSoup(html)
		assignments = []
		scores = []
		rows = soup.find_all("tr", "NormalRowEven")
		odds=soup.find_all("tr", "NormalRow")
		for i in odds:
			rows.append(i)
		#get all rows from soup
		totalscores = [anyrow for anyrow in rows if (anyrow.find("td", {"align": "center"}) == None and anyrow.find("td",{"align": "right"}) != None)]
		for score in totalscores:
			scoreinfo = {}
			scoreinfo["name"] = (score.contents[0].text)
			score1 = (score.contents[1].text)
			scoreinfo["score"] = self.to_number(score1)
			scoreinfo["maxscore"]= self.to_number(score.contents[2].text)
			scoreinfo["percent"] = float(score.contents[3].text)
			scores.append(scoreinfo)
		#gets the total / cumulative grades
		rows=[anyrow for anyrow in rows if (anyrow.find("td", {"align" : "center"})!= None  and anyrow.contents[0].text.encode('ascii','ignore').isdigit())]
		for assignment in rows:
			assignmentinfo = {}
			assignmentinfo["name"] = (assignment.contents[1].text)
			assignmentinfo["type"] = (assignment.contents[2].text)
			score=assignment.contents[4].text.encode('ascii','ignore')
			assignmentinfo["score"] = self.to_number(score)
			assignmentinfo["maxscore"] = int(assignment.contents[5].text) 
			assignmentinfo["missing"] = True if score =="[]" else False
			if assignmentinfo["maxscore"] != 0:
				assignmentinfo["percent"] = ('%.2f' % ((float (assignmentinfo["score"])/ float (assignmentinfo["maxscore"]))*100)) + "%"
			else:
				assignmentinfo["percent"] = "100%"
			graded=assignment.contents[8].text.encode('ascii','ignore')
			assignmentinfo["graded"]=True if graded=="Yes" else False
			assignments.append(assignmentinfo)
		assignments=sorted(assignments, key=lambda assignment: assignment["name"])
		#gets the individual assignments
		return {"totalscores":scores , "assignments":assignments}

	def to_number(self,s):
		try:
			return int(float(s))
		except ValueError:
			return 0

	def __getPageHTML(self,url):
		with self.session as s:
			request = s.get(url)
			string=request.text.encode('ascii','ignore')
			return string

