from flask import Flask,render_template,url_for,request,session,redirect,json
from flask.ext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'onlinetestseries'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

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
    try:
        _id=request.form["inputId"]
        _password=request.form["inputPassword"]

        if _id and _password:

            conn=mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('sp_createUser', (_id,_password))
            data = cursor.fetchall()

            if len(data) is 0:
              conn.commit()
              return json.dumps({'message': 'User created successfully !'})
            else:
              return json.dumps({'error': str(data[0])})
         else:
              return json.dumps({'html': '<span>Enter the required fields</span>'})

     except Exception as e:
     return json.dumps({'error': str(e)})
     finally:
     cursor.close()
     conn.close()
    return render_template('register.html')

if __name__ == '__main__':
    app.secret_key="mySecret"
    app.run(debug=True)
