from flask import Flask, request, render_template, url_for, flash
from flask_cors import CORS
from flask_restful import Resource, Api
from flask_bootstrap import Bootstrap
import json
import requests


app = Flask(__name__)
api = Api(app)

app.config["SECRET_KEY"] = "mysecret"

# Makes it easy to implement boostrap
Bootstrap(app)
# Makes it possible to send POST requests from javascript outside this service.
CORS(app)

########################### DELIVERY UI #################################
@app.route('/delivery')
def index():
    percent = "50"
    # TODO hent inn data fra database
    return render_template("index.html", percent=percent)


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


@app.route('/ETA', methods=["POST"])
def handleETArequest():
    print(request.data)

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
    app.run(debug=True)
