
import requests
import json
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

API_ENDPOINT = "http://192.168.99.100:4020/ETA"

testData = {'sender': 'Alice', 
    'receiver': 'Bob', 
    'message': 'We did it!'}

headerr = {'Content-Type': 'application/json'}

# testData.append({
#     "c_id": 1,
#     "address":{
#         "street": "Varaberget",
#         "street_nr": 18,
#         "postal_code": 4046
#     }
# })

@app.route("/")
def index():
    return "Frontpage for ETA-test."

@app.route('/sendtestdataETA', methods=["GET"])
def sendtestdataETA():
    print("Hei")
    r = requests.post(url = API_ENDPOINT, json=json.dumps(testData), headers=headerr)
    return "Sending data: Status code: " + str(r.status_code)


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=4040)