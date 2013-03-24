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
		self.periods=self.aeries.getPeriods()
		
	