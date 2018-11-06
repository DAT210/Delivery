from flask import Flask, request, make_response
from flask_cors import CORS
from flask_restful import Resource, Api, abort
from random import randint
import json, requests, sys, logging, time, route, delivery, geocoder, pickle


app = Flask(__name__)
api = Api(app)
CORS(app) #Makes it possible to send POST requests from javascript outside this service.

app.config["GOOGLE_MAPS_API_KEY"] = "AIzaSyCuIwZpGcrFtXgGk_rk4MJeW7Musdj9Jm8"
app.config["GOOGLE_MAPS_API_URL"] = "https://maps.googleapis.com/maps/api/directions/json?"
app.config["ORIGIN_ADDRESS"] = "Sandnes"
app.config["TRANSPORT_METHODS"] = ["driving", "walking", "transit"]

cache = {} # KEY: order_id, VALUE: Delivery object


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

#Fetches new job for the delivery client from cache
class delivery_client_getjob(Resource):
    def get(self):
        for key, value in cache.items():
            if value.status == "WAITING":
                value.status = "TAKEN"

                resp = {
                    "order_id": key,
                    "delivery_method": value.delivery_method,
                    "address": value.destination,
                    "route": value.route.waypoints
                }
                return resp
        return False

#Receives updated cooridnates from the delivery client
class delivery_client_update(Resource):
    def get(self):
        lat, lng, order_id, status = request.args.get('lat'), request.args.get("lng"), request.args.get("oid"), request.args.get("status")
        origin = {"lat": lat, "long": lng}

        print("Recieved update on order {}. New coordinates: {}, {}".format(order_id, origin["lat"], origin["long"]))

        if status == "DELIVERED":
            print("Order {} has been delivered.".format(order_id))
            del cache[order_id]
            return "Order has been delivered"
        
        cache[order_id].origin_coord = origin
        cache[order_id].status = status
    
        return

#Receives finalized order and adds it to db and cache
class new_order(Resource):
    def post(self):
        global cache
        # Insert new order with metod to DB

        order_id = request.form["order_id"]
        delivery_method = request.form["delivery_method"]
        address = str(request.form["address"])

        if request.form["aborted"] == "True":
            print("Order aborted")
            return "Order successfully aborted"
        else:
            new_route = route.Route(address, delivery_method)
            new_delivery = delivery.Delivery(delivery_method, address, order_id, "WAITING", new_route)
            cache[order_id] = new_delivery
            print("Order created: {}".format(order_id))
            return "SUCCESS: ORDER {} CREATED".format(order_id)

#Gives the current ETA and coordinates for a specific delivery
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


api.add_resource(eta_for_delivery_methods, '/delivery/methods/eta')
api.add_resource(delivery_client_getjob, '/delivery/client/job')
api.add_resource(eta_for_order, '/delivery/<int:order_id>/eta')
api.add_resource(delivery_client_update, '/delivery/client/update')
api.add_resource(new_order, '/delivery/neworder')  # POST REQ


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=1337)
