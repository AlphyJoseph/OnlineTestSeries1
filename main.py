from flask import Flask,render_template,request,session,json,redirect,flash,url_for
from sqlalchemy.orm import sessionmaker
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

@app.route('/homeScreen')
def home():
  if not session.get('logged_in'):
    return render_template('index.html')
  else:
    return render_template('LIST.html')

@app.route('/home', methods=['POST'])
  if request.method == 'POST' :
    POST_SEM = str(request.form['sem'])

    DBsession = Session()
    query =
        
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
	return redirect(url_for('homeScreen'))

@app.route('/registerScreen')
def registerScreen():
	if not session.get('logged_in'):
		return render_template('register.html')
	else:
		return render_template('LIST.html')

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

#Logs user out
@app.route("/logout")
def logout():
    session['logged_in'] = False
    return redirect(url_for('index'))

if __name__ == '__main__':
	
	app.run(debug=True, threaded=True)
