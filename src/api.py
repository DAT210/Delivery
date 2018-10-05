from flask import Flask, request
from flask_cors import CORS
from flask_restful import Resource, Api
import json, requests

app = Flask(__name__)
api = Api(app)
CORS(app) #Makes it possible to send POST requests from javascript outside this service.

app.config["GOOGLE_MAPS_API_KEY"] = "AIzaSyA-z2Kd25PFPMs3gCSpC6bzPBazgSWtLGY"
app.config["GOOGLE_MAPS_API_URL"] = "https://maps.googleapis.com/maps/api/directions/json?"
app.config["ORIGIN_ADDRESS"] = "Sandnes"
app.config["TRANSPORT_METHODS"] = ["driving", "walking", "transit"]


class ETA(Resource):
    def get(self):
        response = {}
        addr = request.args.get('address')
        for t_m in app.config["TRANSPORT_METHODS"]:
            request_url = app.config["GOOGLE_MAPS_API_URL"] + "origin={}&destination={}&mode={}&key={}".format(app.config["ORIGIN_ADDRESS"], addr, t_m, app.config["GOOGLE_MAPS_API_KEY"])
            content = json.loads(requests.get(request_url).content)
            distance = content["routes"][0]["legs"][0]["distance"]["text"]
            duration = content["routes"][0]["legs"][0]["duration"]["text"]

            # Geocode status (Checks if origin and destination locations are valid)
            # status_location1, status_location2 = content["geocoded_waypoints"][0]["geocoder_status"], content["geocoded_waypoints"][1]["geocoder_status"] 

            response[t_m] = {
                "distance": distance,
                "eta": duration
            }
        return response

api.add_resource(ETA, '/delivery/eta')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
