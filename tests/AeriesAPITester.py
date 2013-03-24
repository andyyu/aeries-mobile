#Add tests for AeriesAPI here 
import AeriesAPI
s=AeriesAPI.AeriesAPI('annuj@sbcglobal.net','shivamt')

#test to check if periods are correctly fetched
#
#print "Classes: "
#print s.getPeriods()

print "Bio Assignments:"
print s.getPeriodAssignments('https://mystudent.fjuhsd.net/GradebookStuScores.asp?cache=3%2F23%2F2013+10%3A34%3A02+PM&GrdBk=2100004')
#add new tests here