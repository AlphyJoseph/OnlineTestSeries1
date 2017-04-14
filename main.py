from flask import Flask,render_template,request,session,json,redirect,flash,url_for
from sqlalchemy.orm import sessionmaker,load_only
from DB_schemas  import *
import hashlib, uuid
import os

#Connecting to the database
engine = create_engine('sqlite:///onlineTestSeries.db', echo=True)
Session = sessionmaker(bind=engine)

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config.from_object(__name__)
DEBUG = True


@app.route('/')
def index():
	if not session.get('logged_in'):
		return render_template('index.html')
	else:
		return render_template('LIST.html')

###################################################################################################
        
@app.route('/login', methods=['POST'])
def login():
	print "In login"
	if request.method=='POST':
		POST_USN = str(request.form['userid'])
		POST_PASSWORD = str(request.form['pass'])

		#Password hashing
		hash_password = hashlib.sha512(POST_PASSWORD).hexdigest()

		print "Created session"
		DBsession = Session()
		query = DBsession.query(User).filter(User.usn.in_([POST_USN]), User.password.in_(([hash_password])))
		result = query.first()

		if result:
			session['logged_in'] = True
		else:
			flash('Invalid Credentials....Please register and proceed to Login')
	return redirect(url_for('home'))

########################################################################################################
@app.route('/hScreen')
def home():
  if not session.get('logged_in'):
    return render_template('index.html')
  else:
    return render_template('LIST.html')

#########################################################################################################



@app.route('/chosenSemester/<int:sem>')
def chosenSemester(sem):
  DBsession = Session()
  subs = DBsession.query(Semester).filter(Semester.sem.in_([sem]))
  subjects = subs.first()
 

  subjects_list = subjects.subjects.split(',')

    
  if not session.get('logged_in'):
	return render_template('index.html')
  else:
	return render_template('subjects.html',subjects=subjects_list, sem = sem)

#########################################################################################################

@app.route('/chosenSemester/<int:sem>/<string:subject>')
def chosenSubject(sem, subject):
	DBsession = Session()
	quest = DBsession.query(Subjects).filter(Subjects.sub.in_([subject]))
	questions = ques.first()

	questions_list = quest.ques.op1.op2.op3


	if not session.get('logged_in'):
		return render_template('index.html')
	else:
		return render_template('subjects.html',subjects=subjects_list, chosenSubject=subject, sem=sem, questions=questions_list)


####################################################################################################

@app.route('/registerScreen')
def registerScreen():
	if not session.get('logged_in'):
		return render_template('index.html')
	else:
		return render_template('LIST.html')

######################################################################################################

@app.route('/register',methods=['GET','POST'])
def register():
	if request.method=='POST':
		USN = str(request.form['userID'])
		PASSWORD = str(request.form['pass'])

		#Password hashing
		hash_password = hashlib.sha512(PASSWORD).hexdigest()

		DBsession = Session()
		query = DBsession.query(User).filter(User.usn.in_([USN]) )
		result = query.first()

		if result:
			flash('User already exists! Please login')
		else:
			hash_password = hashlib.sha512(PASSWORD).hexdigest()
			user = User(USN,hash_password)
			DBsession.add(user)
			DBsession.commit()
			flash('User Registration Successful!')
	return render_template('index.html')

#####################################################################################Logs user out
@app.route("/logout")
def logout():
    session['logged_in'] = False
    return redirect(url_for('index'))

if __name__ == '__main__':
	
	app.run(debug=True, threaded=True)
