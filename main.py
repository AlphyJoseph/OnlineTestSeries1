from flask import Flask,render_template,url_for,request,session,redirect


app = Flask(__name__)


@app.route('/')
def index():
    if 'username' in session:
        return ""
    return render_template('index.html')
@app.route('/login')
def login():
    return ""
@app.route('/register')
def register():
    return ""

if __name__ == '__main__':
    app.secret_key="mySecret"
    app.run(debug=True)
