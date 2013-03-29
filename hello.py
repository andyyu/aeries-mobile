from flask import Flask
from flask import render_template
from flask import request
from flask import g
from flask import session
import AeriesAPI

app = Flask(__name__)
Flask.secret_key='Develop'

@app.route('/')
def index():
	return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
	if request.method=='POST':
		user=request.form['user']
		pw=request.form['pass']
		aeries=AeriesAPI.AeriesAPI(user,pw)
		session.aeries=aeries
		return render_template('gradebook.html', user=user, pw=pw, periods=aeries.getPeriods())

@app.route('/class/<class_id>')
def period(class_id):
	print session.aeries
	#assignments=session.aeries.getPeriodAssignments(class_id)
	return render_template('gradebook.html', assignments="hello")

if __name__ == '__main__':
	app.debug = True
	app.run()