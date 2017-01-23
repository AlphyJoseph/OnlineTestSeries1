from flask import Flask,render_template,request,session,json,redirect,flash,url_for
from flaskext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash
mysql = MySQL()


app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'OnlineTestSeries'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
app.secret_key="mySecret"

@app.route('/')
def index():
    if 'username' in session:
        return ""
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

        conn=mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('sp_createUser1', (_id,_hashed_password))
        data = cursor.fetchall()

        if len(data) is 0:
          conn.commit()
          flash('User Created Successfully')
          return render_template('')
         # return json.dumps({'message': 'User created successfully !'})
        else:
        	flash('Error! User already exixts!')
        	return redirect(url_for('login'))
          #return json.dumps({'error': str(data[0])})

      else:
      		flash('Enter required fields')
      		return redirect(url_for('register'))
       # return json.dumps({'html': '<span>Enter the required fields</span>'})

    

      cursor.close()
      conn.close()
  return render_template('register.html')


if __name__ == '__main__':
    
    app.run(debug=True)
