from flask import Flask, request, render_template, url_for, flash, g
from flask_cors import CORS
from flask_restful import Resource, Api
import json
import requests
from deliveryDB import Database
import mysql.connector

app = Flask(__name__)
api = Api(app)

app.config["SECRET_KEY"] = "mysecret"

# Pass inn app.config if you wat to use the database class
app.config["DATABASE_USER"] = "root"
app.config["DATABASE_PASSWORD"] = "root"
app.config["DATABASE_DB"] = "delivery"
app.config["DATABASE_HOST"] = "db"
app.config["DATABASE_PORT"] = "3306"

# Makes it possible to send POST requests from javascript outside this service.
CORS(app)


########################### DATABASE EXAMPLE #################################

@app.route('/insert_delivery')
def insertDelivery():
    # pass inn config
    db = Database(app.config)
    #did, aid, order_id, customer_id, price, vehicle, order_delivered, order_ready
    data1 = [1, 1, 1, 1, 59.99, "Car", 0, 0]
    data2 = [2, 2, 2, 2, 79.99, "Car", 0, 0]
    db.insert_delivery(data1)
    return "Inserting delivery into database..."

@app.route('/query_delivery')
def queryDelivery():
    db = Database(app.config)
    return db.query_delivery()

@app.route('/query_address')
def queryAddress():
    db = Database(app.config)
    return db.query_address()

@app.route('/insert_address')
def insertAddress():
    data1 = [1, 'Sandnes', 4326, 'MyyyyyVeien', 12, '']
    data2 = [2, 'Stavanger', 4032, 'Gauselarmen', 14, 'B']
    db = Database(app.config)
    db.insert_address(data1)
    return "Inserting address into database..."





###########################        END       #################################


########################### DELIVERY UI #################################

# hmmmmmmmmm! http://localhost:6969/delivery/1/delivery//eta
@app.route('/delivery/<int:order_id>/map')
def index(order_id):
    return render_template("index.html")

i = 0
@app.route('/delivery/<int:order_id>/eta')
def eta(order_id):
    global i
    if (i == 0):
        data = {"lat": 58.847426, "lng": 5.7535204,
                 "eta": {"text": "12min", "val": 123123}}
        i += 1
    elif (i==1):
        data = {"lat": 58.867426, "lng": 5.7535204,
                "eta": {"text": "12min", "val": 123123}}
        i += 1
    elif (i == 2):
        data = {"lat": 58.887426, "lng": 5.7535204,
                "eta": {"text": "12min", "val": 123123}}
        i += 1
    else:
        data = {"lat": 58.897426, "lng": 5.7535204,
                "eta": {"text": "12min", "val": 123123}}
    return json.dumps(data)


@app.route('/')
def delivery():
    eta = 20
    percent = 0
    flash("ETA is " + str(eta) + " minutes")
    return render_template("index.html", eta=eta, percent=percent)


@app.route('/1')
def deliver1():
    eta = 10
    percent = 50
    flash("ETA is " + str(eta) + " minutes")
    return render_template("index.html", eta=eta, percent=percent)


@app.route('/2')
def delivery2():
    eta = 2
    percent = round(((20-eta)/20)*100)
    flash("ETA is " + str(eta) + " minutes")
    return render_template("test.html", eta=eta, percent=percent)




########################### DELIVERY UI #################################

#TODO: Implement functioncalls depending on routes and content of http requests



##########Just for testing#################################################

@app.route("/testing")
def testing():
    return 'Yes, you got here'

@app.route("/testingget", methods=["GET"])
def testingget():
    return 'Yes, you got here with the text: ' + request.args.get("test")
@app.route("/testingpost", methods=["POST"])
def testingpost():
    testvalue = "Nothing"
    if "aKey" in request.form :
        testvalue = request.form["aKey"]
    return "you got here " + testvalue 


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=6969)
