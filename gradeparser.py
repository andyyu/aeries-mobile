from bs4 import BeautifulSoup
import parser
soup = BeautifulSoup(class_grades(periodnum))
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
	return classinfo
parse_classes()
print classes