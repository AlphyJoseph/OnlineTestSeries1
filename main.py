from flask import Flask,render_template,request,session,json,redirect,flash,url_for
import sqlite3 as sql
from werkzeug import generate_password_hash, check_password_hash


app = Flask(__name__)
app.secret_key="mySecret"

@app.route('/')
def index():
    if 'userID' in session:
        return render_template('LIST.html')
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('index.html')

@app.route('/register',methods=['GET','POST'])
def register():
  if request.method=='POST':

    _id=request.form["userID"]
    _password=request.form["pass"]
    _hashed_password = generate_password_hash(_password)
    con = sql.connect("onlinetestseries.db")

    if _id and _password:
      cur = con.execute("SELECT USN from USERS")
      for USN in cur:
        print USN[0]
        if(USN[0] == _id):
          flash('User already exixts! Please Login')
          con.close()
          return redirect(url_for('login'))

      con.execute("INSERT INTO USERS VALUES(?,?)",(_id,_hashed_password))
      
      flash('User Created Successfully')
      con.commit()
      con.close()
      return render_template('LIST.html')
    else:
        flash('Enter required fields')
        return redirect(url_for('register'))
   
  return render_template('register.html')


if __name__ == '__main__':
    
    app.run(debug=True, threaded=True)
