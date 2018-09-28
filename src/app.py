from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World! We have Flask in a Docker container!'

@app.route("/testing")
def testing():
    return 'Yes, you got here'

@app.route("/testingget", methods=["GET"])
def testingget():
    return 'Yes, you got here with '+ request.args.get("test")

@app.route("/testingpost", methods=["POST"])
def testingpost():
    return 'Yes, you got here'

@app.route("/testing", methods=["POST, GET"])
def testinggetandpost():
    return 'Yes, you got here'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
