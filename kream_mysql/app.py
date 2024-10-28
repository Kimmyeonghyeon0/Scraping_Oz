from flask import Flask, render_template
import pymysql


app = Flask(__name__)

connection = pymysql.connect(
    host = '127.0.0.1',
    user = 'root',
    password = '00915',
    db = 'kream',
    charset = 'utf8mb4'
)

cur = connection.cursor()
sql = "SELECT * FROM kream"
cur.execute(sql)

kream_date = cur.fetchall()

@app.route('/')
def index():
    return render_template('index.html, data_list = kream_date')



if __name__ == '__main__':
    app.debug = True
    app.run

