
import requests
import json
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

API_ENDPOINT = "http://192.168.99.100:4020/ETA"

headerr = {'Content-Type': 'application/json'}

testData = ({
    "c_id": 1,
    "address":{
        "street": "Gauselarmen",
        "street_nr": "14B",
        "postal_code": 4032
    }
})

@app.route("/")
def index():
    return "Frontpage for ETA-test."

@app.route('/sendtestdataETA', methods=["GET"])
def sendtestdataETA():
    print("Hei")
    r = requests.post(url = API_ENDPOINT, json=json.dumps(testData), headers=headerr)
    return "Sending data: Status code: " + str(r.status_code) + " " + r.text


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=4040)