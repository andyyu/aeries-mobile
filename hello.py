from flask import Flask
from flask import render_template
from flask import request
import Student

app = Flask(__name__)
global student #should find an alternative, but can't think of one

@app.route('/')
def index():
	return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
	if request.method=='POST':
		user=request.form['user']
		pw=request.form['pass']
		student=Student.Student(user,pw)
		return render_template('gradebook.html', user=user, pw=pw, periods=student.periods)

@app.route('/class/<class_id>')
def period(class_id):
	pass

if __name__ == '__main__':
	app.debug = True
	app.run()