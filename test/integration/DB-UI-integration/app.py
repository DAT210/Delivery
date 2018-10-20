import mysql.connector
from flask import Flask, g, request, render_template, url_for
from flask_bootstrap import Bootstrap
import json
import datetime
import unittest


app = Flask(__name__, template_folder='templates')
# Makes it easy to implement boostrap
Bootstrap(app)

app.config["SECRET_KEY"] = "mysecret"
app.config["DATABASE_USER"] = "root"
app.config["DATABASE_PASSWORD"] = "root"
app.config["DATABASE_DB"] = "testdb"
app.config["DATABASE_HOST"] = "db"
app.config["DATABASE_PORT"] = "3306"

def get_db():
    if not hasattr(g, "_database"):
        g._database = mysql.connector.connect(host=app.config["DATABASE_HOST"],
                                              user=app.config["DATABASE_USER"],
                                              password=app.config["DATABASE_PASSWORD"],
                                              database=app.config["DATABASE_DB"],
                                              port=app.config["DATABASE_PORT"]
                                              )
    return g._database

def calulcate_ETA(recieved):
    now = datetime.datetime.now()
    expected = recieved + datetime.timedelta(minutes=15)
    eta = (expected - now)
    x = (now - recieved)
    percent = int((x/eta)*100)
    return eta, percent

    
# Can slettes kommer ikke til å bruke
# class TestCalculateETA(unittest.TestCase):
#     def test(self):
#         testCase = datetime.datetime.now() - datetime.timedelta(minutes=15)
#         result_eta = datetime.datetime.now() + datetime.timedelta(minutes=15)
#         self.assertEqual(calulcate_ETA(testCase), result_eta,  0)



@app.route('/delivery/<int:id>')
def index(id):
    db = get_db()
    cur = db.cursor()
    try:
        cur.execute("SELECT tid, vehicle, _time FROM transport WHERE tid={}".format(id))
        row = cur.fetchone()
        recieved = row[2]
        eta , percent = calulcate_ETA(recieved)
        return render_template("index.html", eta=str(eta), percent=percent)
    except mysql.connector.Error:
        return False
    finally:
        cur.close()


if __name__ == '__main__':
    #unittest.main()
    app.run(debug=True, host='0.0.0.0', port=80)

