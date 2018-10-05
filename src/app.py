from flask import Flask, request
from flask_cors import CORS
from flask_restful import Resource, Api
import json
import requests
app = Flask(__name__)
api = Api(app)
# Makes it possible to send POST requests from javascript outside this service.
CORS(app)


@app.route('/')
def hello_world():
    return 'Hello World! We have Flask in a Docker container!'

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
    app.run(debug=True, host='0.0.0.0', port=)
