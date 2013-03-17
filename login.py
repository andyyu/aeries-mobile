from requests import session
import unicodedata

payload = {
    'UserName': "",
    'Password': ""
}

with session() as c:
    c.post('https://mystudent.fjuhsd.net/loginprochome.asp', data=payload)
    request = c.get('https://mystudent.fjuhsd.net/GradebookSummary.asp')
    string=request.text.encode('ascii','ignore')
    f = file ('gradebook.html','w')
    f.write(string)
def getgrades(periodurl, filename):
	request = c.get(periodurl)
	string=request.text.encode('ascii','ignore')
	f = file (filename,'w')
	f.write(string)
