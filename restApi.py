#with flask

#creating user table through a mysql db that reads it and constitute rest api

#columns: id, name, mail, phone, date


from  flask import Flask
from flask import request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '12345678'
app.config['MYSQL_DB'] = 'pythonProject db'

mysql = MySQL(app)

@app.route("/user")
def users():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM user_info''')
    rows = cur.fetchall()
    result = ''
    for row in rows:
        rv=''
        for j in row:
            rv=rv + '&emsp;' + '&emsp;' + str(j)
            print(j)
        result = result + rv + '<br>'
    return result



