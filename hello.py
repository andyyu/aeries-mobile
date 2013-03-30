import os
from flask import Flask
from flask import render_template
from flask import request
from flask import g
from flask import session
from simplekv.memory import DictStore
from flaskext.kvsession import KVSessionExtension
import Student
import AeriesAPI

store = DictStore()
app = Flask(__name__)
Flask.secret_key='Develop'

KVSessionExtension(store, app)

@app.route('/')
def index():
	return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
	if request.method=='POST':
		user=request.form['user']
		pw=request.form['pass']
		student=Student.Student(user,pw)
		session["user"]=user
		session["pw"]=pw
		return render_template('gradebook.html', user=user, pw=pw, periods=student.periods)

@app.route('/class/<class_id>')
def period(class_id):
	assignments=[]
	student=Student.Student(session["user"],session["pw"])
	for period in student.periods:
		if(period["class_id"]==class_id):
			period_name=period["name"]
	assignments=student.aeries.getPeriodAssignments(class_id)
	return render_template('class.html', assignments=assignments, period_name=period_name)

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port, debug=True)