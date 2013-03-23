import AeriesAPI
class Student:
	def __init__(self, user, pw):
		self.username=user
		self.password=pw
		self.aeries= AeriesAPI.AeriesAPI(user,pw)
		self.classes=self.aeries.getPeriods()

	

s=Student('annuj@sbcglobal.net','shivamt')
s.login()