from flask import Flask, request
from flask_cors import CORS
from flask_restful import Resource, Api, abort
import json, requests, sys, logging, time

app = Flask(__name__)
api = Api(app)
CORS(app) #Makes it possible to send POST requests from javascript outside this service.

app.config["GOOGLE_MAPS_API_KEY"] = "AIzaSyA-z2Kd25PFPMs3gCSpC6bzPBazgSWtLGY"
app.config["GOOGLE_MAPS_API_URL"] = "https://maps.googleapis.com/maps/api/directions/json?"
app.config["ORIGIN_ADDRESS"] = "Sandnes"
app.config["TRANSPORT_METHODS"] = ["driving", "walking", "transit"]

duration = 0
"http://127.0.0.1:1337?oid=1"
#App.py henter adresse på ordre og kundeinfo

class ETA(Resource):
    def get(self):
        global duration
        response = {}
        addr = request.args.get('address')
        if addr:
            for transport_method in app.config["TRANSPORT_METHODS"]: 
                # Geocode status (Checks if origin and destination locations are valid)
                content = calculateETA(app.config["ORIGIN_ADDRESS"],addr, transport_method)
                status_location1, status_location2 = content["geocoded_waypoints"][0]["geocoder_status"], content["geocoded_waypoints"][1]["geocoder_status"]
                if status_location2 != "OK" and status_location1 != "OK":
                    return {"error": status_location2}
                distance = content["routes"][0]["legs"][0]["distance"]["text"]
                duration = content["routes"][0]["legs"][0]["duration"]["text"]


                response[transport_method] = {
                    "distance": distance,
                    "eta": duration
                }
            return response
        else:
            abort(400, message="Address can not be empty")



class Status(Resource):
    def get(self):
        global duration

        return ""
        
def calculateETA(orgin, destination, mode):
    request_url = app.config["GOOGLE_MAPS_API_URL"] + "origin={}&destination={}&mode={}&key={}".format(orgin, destination, mode, app.config["GOOGLE_MAPS_API_KEY"])
    return json.loads(requests.get(request_url).content)

api.add_resource(ETA, '/delivery/eta')
api.add_resource(Status, '/delivery/status')


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=1337)
