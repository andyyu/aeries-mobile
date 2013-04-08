#Add tests for AeriesAPI here 
import AeriesAPI
s=AeriesAPI.AeriesAPI('annuj@sbcglobal.net','shivamt')
s.login()

#test to check if periods are correctly fetched
#
#print "Classes: "
#print s.getPeriods()

print "Bio Assignments:"
print s.getPeriodAssignments('2100004')
#add new tests here