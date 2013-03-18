from bs4 import BeautifulSoup
import login
f = file ('gradebook.html','r')
soup = BeautifulSoup(f.read())
rows = soup.find_all("tr", "NormalClickableRowEven")
classes = []

def parse_classes():
	for period in rows:
		classes.append(parse_classinfo(period))

def parse_classinfo(period):
	classinfo = {}
	classinfo["name"] = (period.contents[1].text.encode('ascii','ignore'))
	classinfo["percentgrade"] = (period.contents[5].text.encode('ascii','ignore'))
	classinfo["lettergrade"] = (period.contents[6].text.encode('ascii','ignore'))
	classinfo["missingassign"] = (period.contents[7].text.encode('ascii','ignore'))
	classinfo["classurl"] = (period.contents[1].contents[0].href)
	return classinfo

def class_grades(periodnum):
	login.getgrades(classes[periodnum]["classurl"], classes[periodnum]["name"]+".html")
	g = file ('classes[periodnum]["name"]+".html','r')
	return g

def parse_grades(periodnum):
	gradesoup = BeautifulSoup(class_grades(periodnum).read())
	rows = soup.find_all("tr", "NormalRow")

parse_classes()
print classes
