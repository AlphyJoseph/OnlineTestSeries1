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

      if _id and _password:

        con = sql.connect("OnlineTestSeries.db")
      cur = con.cursor()
      cur.execute("SELECT USN from Users")
      data=cur.fetchall()
      for USN in data:
        if(USN==_id):
          flash('User already exixts! Please Login')
          break
          return redirect(url_for('login'))

       
        else:
          cur.execute("INSERT INTO Users(USN,password) VALUES(?,?)",(_id,_hashed_password))
          con.commit()
          flash('User Created Successfully')
          break
          return render_template('LIST.html')
         
        
      else:
          flash('Enter required fields')
          return redirect(url_for('register'))
     
      con.close()
  return render_template('register.html')


if __name__ == '__main__':
    
    app.run(debug=True)
