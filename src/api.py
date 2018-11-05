from flask import Flask, request, make_response
from flask_cors import CORS
from flask_restful import Resource, Api, abort
from random import randint
import json, requests, sys, logging, time, route, delivery, geocoder

app = Flask(__name__)
api = Api(app)
CORS(app) #Makes it possible to send POST requests from javascript outside this service.

app.config["GOOGLE_MAPS_API_KEY"] = "AIzaSyCuIwZpGcrFtXgGk_rk4MJeW7Musdj9Jm8"
app.config["GOOGLE_MAPS_API_URL"] = "https://maps.googleapis.com/maps/api/directions/json?"
app.config["ORIGIN_ADDRESS"] = "Sandnes"
app.config["TRANSPORT_METHODS"] = ["driving", "walking", "transit"]

cache = {} # KEY: order_id, VALUE: Delivery object

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




class eta_for_delivery_methods(Resource):
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

#TODO fetch job from available jobs in cache
#For now i just use a static list of orders.
class delivery_client_getjob(Resource):
    def get(self):
        for order in temp_jobs:
            if order["status"] == "WAITING":
                order["status"] = "TAKEN"
                return order
        return "No jobs available"

    

class update_eta_for_order(Resource):
    def get(self, order_id):
        lat, lng, order_id, status = request.args.get('lat'), request.args.get("long"), request.args.get("oid"), request.args.get("status")
        origin = {"lat": lat, "long": lng}

        print("Recieved update on order {}. New coordinates: {}, {}".format(order_id, origin["lat"], origin["long"]))

        if status == "delivered":
            print("Order {} has been delivered.".format(order_id))
            del cache[order_id]
            return "Order has been delivered"
        
        cache[order_id].origin_coord = origin
        cache[order_id].status = status
    
        return


class new_order(Resource):
    def post(self):
        global cache
        # Insert new order with metod to DB

        order_id = request.form["order_id"]
        delivery_method = request.form["delivery_method"]
        address = request.form["address"]

        if request.form["aborted"] == "True":
            print("Order aborted")
            return "Order successfully aborted"
        else:
            new_delivery = delivery.Delivery(delivery_method, address, order_id, "Recieved")
            cache[order_id] = new_delivery
            print("Order created: {}".format(order_id))
            return "SUCCESS: ORDER {} CREATED".format(order_id)

        


class eta_for_order(Resource):
    def get(self, order_id):
        global cache
        order = cache[str(order_id)]
        
        destination = order.destination_coord
        method = order.delivery_method
        origin = order.origin_coord

        print("DEST: {}".format(destination))
        print("ORI: {}".format(origin))

        new_route = route.Route(destination, method, origin, "coord")

        print("New coordinates and ETA for order {}: {}, ETA: {}".format(order_id, origin, new_route.total_duration))

        return {
            "lat": order.origin_coord["lat"],
            "long": order.origin_coord["long"],
            "eta": {
                "text": str(new_route.total_duration) + " minutes",
                "val": new_route.total_duration * 60
            }
        }


class test(Resource):
    def get(self):
        dest = request.args.get("destination")
        # lat = int(request.args.get("lat"))
        # lng = int(request.args.get("lng"))
        # dest = {'lat': lat, 'long': lng}
        # ori = {'lat': 58.8532585, 'long': 5.7329455}
        test_route = route.Route(dest, "driving")

        print("Destination: {}, origin: {}, ETA: {}".format(test_route.destination, test_route.origin, test_route.total_duration))



api.add_resource(eta_for_delivery_methods, '/delivery/methods/eta')
api.add_resource(delivery_client_getjob, '/delivery/client/job')
api.add_resource(eta_for_order, '/delivery/<int:order_id>/eta')
api.add_resource(update_eta_for_order, '/delivery/<int:order_id>/coord')
api.add_resource(new_order, '/delivery/neworder')  # POST REQ

api.add_resource(test, '/test')




if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=1337)
