import requests
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def static_index():
    return render_template("testingdelivery.html")

@app.route('/get')
def testget():
    return requests.get('http://127.0.0.1:4020').text

@app.route('/gettoolbox')
def testget():
    return requests.get('http://192.168.99.100:4020').text

@app.route('/post')
def testpost():
    return requests.post('http://127.0.0.1:4020/testingpost', data = {"aKey":"aValue"}).text

@app.route('/posttoolbox')
def testpost():
    return requests.post('http://192.168.99.100:4020/testingpost', data = {"aKey":"aValue"}).text

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
