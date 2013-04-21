#Add tests for AeriesAPI here 
import AeriesAPI
s=AeriesAPI.AeriesAPI('annuj@sbcglobal.net','shivamt')
s.login()

#test to check if periods are correctly fetched
#
#print "Classes: "
#print s.getPeriods()

print "Spanish Assignments:"
print s.getPeriodAssignments('3430307')
#add new tests here