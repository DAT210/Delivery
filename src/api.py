from flask import Flask, request, make_response
from flask_cors import CORS
from flask_restful import Resource, Api, abort
import json, requests, sys, logging, time, route

app = Flask(__name__)
api = Api(app)
CORS(app) #Makes it possible to send POST requests from javascript outside this service.

app.config["GOOGLE_MAPS_API_KEY"] = "AIzaSyA-z2Kd25PFPMs3gCSpC6bzPBazgSWtLGY"
app.config["GOOGLE_MAPS_API_URL"] = "https://maps.googleapis.com/maps/api/directions/json?"
app.config["ORIGIN_ADDRESS"] = "Sandnes"
app.config["TRANSPORT_METHODS"] = ["driving", "walking", "transit"]

#Temporary until db integration is ok.
temp_jobs = [{
        "order_id": 1,
        "status": "WAITING",
        "legs": [
            {
                "latitude": 58.96627642581798,
                "longitude": 5.730213685769627,
                "time": 25
            },
            {
                "latitude": 58.95946134959505,
                "longitude": 5.734076066751072,
                "time": 30
            },                {
                "latitude": 58.95600904377245,
                "longitude": 5.735706849832127,
                "time": 0
            }
        ]
    }]

class methods_eta(Resource):
    def get(self):
        destination_address = request.args.get('address')
        response = {}

        for method in app.config["TRANSPORT_METHODS"]:
            try:
                best_route = route.Route(destination_address, method)
            except ValueError as e:
                return make_response(json.dumps({'message': e.args[0]}), 400)
            
            response[method] = {
                "eta": best_route.total_duration,
                "distance": best_route.total_distance,
                "price": best_route.total_price
            }

        return response


#TODO fetch job from available jobs in db
#For now i just use a static list of orders.
class delivery_client_getjob(Resource):
    def get(self):
        for order in temp_jobs:
            if order["status"] == "WAITING":
                order["status"] = "TAKEN"
                return order
        return "No jobs available"



class delivery_client_update(Resource):
    def get(self):
        lat = request.args.get('lat')
        lng = request.args.get('lng')
        order = request.args.get('orderid')
        print("Got new updates:\nOrder: {}\nLat: {}, Lng: {}".format(order, lat, lng))
    #TODO send coordinate updates to correct order and update map
    

api.add_resource(methods_eta, '/delivery/methods/eta')
api.add_resource(delivery_client_getjob, '/delivery/client/job')
api.add_resource(delivery_client_update, '/delivery/client/update')


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=1337)
