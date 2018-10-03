from flask import Flask, g
import mysql.connector
import json

app = Flask(__name__)
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

@app.route('/')
def db_test():
    db = get_db()
    cur = db.cursor()
    try:
        cur.execute("SELECT tid, vehicle, ETA FROM transport")
        data = []
        for tid, vehicle, ETA in cur:
            data.append({
                "tid": tid,
                "vehicle": vehicle,
                "ETA": ETA
            })
        return json.dumps(data)
    except mysql.connector.Error:
        return False
    finally:
        cur.close()

############ TESTING #############

@app.route('/getETA/<id>', methods=["GET"])
def getETA(id):
    db = get_db()
    cur = db.cursor()
    sql = "SELECT vehicle, ETA FROM transport WHERE tid={}".format(id)
    try:
        cur.execute(sql)
        row = cur.fetchone()
        return json.dumps(row)
    except mysql.connector.Error:
        return False
    finally:
        cur.close()

@app.route('/getVehicles')
def getVehicles():
    db = get_db()
    cur = db.cursor()
    try:
        sql = "SELECT DISTINCT(vehicle) FROM transport"
        cur.execute(sql)
        vehicles = []
        for vehicle in cur:
            vehicles.append({
                "vehicle": vehicle
            })
        return json.dumps(vehicles)
    except mysql.connector.Error:
        return False
    finally:
        cur.close()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)

