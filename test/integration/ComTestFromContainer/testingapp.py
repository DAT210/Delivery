import requests
from flask import Flask, render_template
app = Flask(__name__)

app.config["Delivery_IP"] = "delapp"

@app.route('/')
def static_index():
    return render_template("testingdelivery.html")

@app.route('/get')
def testget():
    return requests.get('http://'+app.config["Delivery_IP"]).text

@app.route('/post')
def testpost():
    return requests.post('http://'+app.config["Delivery_IP"]+'/testingpost', data = {"aKey":"aValue"}).text


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
