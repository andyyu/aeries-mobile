#Add tests for AeriesAPI here 
import AeriesAPI
s=AeriesAPI.AeriesAPI('user','pw')
s.login()

#test to check if periods are correctly fetched
#
#print "Classes: "
#print s.getPeriods()

#Test to check if correct period information is fetched
#To test for a different class, put in a different class id.
#To find class id, go to Aeries, right click on the class title (eg. AP-Biology) and copy the link address. Paste the link
#address and look at the last little bit (&GrdBk=2100004). The number after &GrdBk is the classid (eg. 2100004)
print "Spanish Assignments:"
print s.getPeriodAssignments('3430307')#change this classid
#add new tests hereg