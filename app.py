from flask import Flask, render_template, request, redirect, session, url_for
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)

mysql = MySQL(app)

@app.route("/")
def main():
    return render_template('signin.html',msg='')

@app.route("/home")
def home():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM patients WHERE id = 1')
    row = cursor.fetchone()
    return render_template('home.html',row = row)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '########' #root user password for local server
app.config['MYSQL_DB'] = 'medapp' #local database name

@app.route('/login', methods =['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = % s AND password = % s', (username, password))
        row = cursor.fetchone()
        if row:
            print('Logged in successfully !')
            return redirect(url_for('home'))
        else:
            msg = 'Incorrect username / password !'
    return render_template('signin.html', msg = msg)
    
@app.route("/appbok")
def appbok():
    return render_template('appbok.html')

@app.route("/appointment")
def appointment():
    return render_template('appointment.html')

@app.route("/drug")
def drug():
    return render_template('drug.html')

@app.route("/family")
def family():
    return render_template('family.html')

@app.route("/report")
def report():
    return render_template('report.html')

@app.route("/vaccp")
def vaccp():
    return render_template('vaccp.html')

@app.route("/vaccu")
def vaccu():
    return render_template('vaccu.html')

@app.route("/vacopen")
def vacopen():
    return render_template('vacopen.html')

if __name__ == "__main__":
    app.run()
