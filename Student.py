import AeriesAPI

"""
Class representing student, with periods, etc.

Sample call: s=Student('user','pw')
"""
class Student:
	def __init__(self, user, pw):
		self.username=user
		self.password=pw
		self.aeries= AeriesAPI.AeriesAPI(user,pw)
		self.aeries.login()
		self.periods=self.aeries.getPeriods()
	
	def loadAllPeriodAssignments(self):
		assignments=[]
		for period in self.periods:
			period_assignments={}
			period_assignments['id']=period['class_id']
			period_assignments['name']=period['name']
			period_assignments['assignments']=self.aeries.getPeriodAssignments(period['class_id'])
			assignments.append(period_assignments)
		return assignments

		
	