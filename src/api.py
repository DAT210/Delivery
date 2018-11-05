from flask import Flask, request, make_response
from flask_cors import CORS
from flask_restful import Resource, Api, abort
import json, requests, sys, logging, time, route, delivery, pickle

app = Flask(__name__)
api = Api(app)
CORS(app) #Makes it possible to send POST requests from javascript outside this service.

app.config["GOOGLE_MAPS_API_KEY"] = "AIzaSyA-z2Kd25PFPMs3gCSpC6bzPBazgSWtLGY"
app.config["GOOGLE_MAPS_API_URL"] = "https://maps.googleapis.com/maps/api/directions/json?"
app.config["ORIGIN_ADDRESS"] = "Sandnes"
app.config["TRANSPORT_METHODS"] = ["driving", "walking", "transit"]

cache = {} # KEY: order_id, VALUE: Delivery object


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

#TODO fetch job from available jobs in cache
#For now i just use a static list of orders.
class delivery_client_getjob(Resource):
    def get(self):
        for key, value in cache.items():
            resp = 0
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

#Mottar oppdateringer fra client
class order_eta(Resource):
    def get(self, order_id):
        lat, lng, order_id, status = request.args.get('lat'), request.args.get("long"), request.args.get("oid"), request.args.get("status")
        origin = {"lat": lat, "long": lng}

        if status == "delivered":
            del cache[order_id]
            return "Order has been delivered"
        
        cache[order_id]["origin"] = origin
        cache[order_id]["status"] = status
    
        return


class new_order(Resource):
    def post(self):
        # Insert new order with metod to DB

        order_id = request.form["order_id"]
        delivery_method = request.form["delivery_method"]
        address = request.form["address"]

        if request.form["aborted"] == True:
            return "Order aborted"
        else:
            new_route = route.Route(address, delivery_method)
            new_delivery = delivery.Delivery(delivery_method, address, order_id, "WAITING", new_route)
            cache[order_id] = new_delivery

        return "SUCCESS: ORDER {} CREATED".format(order_id)


class update_eta(Resource):
    def get(self, order_id):
        destination = cache[order_id]["destination"]
        method = cache[order_id]["delivery_method"]
        origin = cache[order_id]["origin"]

        new_route = route.Route(destination, method, origin)

        return {
            "lat": origin["lat"],
            "long": origin["long"],
            "eta": {
                "text": str(new_route.total_duration) + " minutes",
                "val": new_route.total_duration * 60
            }
        }


api.add_resource(methods_eta, '/delivery/methods/eta')
api.add_resource(delivery_client_getjob, '/delivery/client/job')
# api.add_resource(delivery_client_update, '/delivery/client/update')
api.add_resource(update_eta, '/delivery/<int:order_id>/eta')
api.add_resource(order_eta, '/delivery/<int:order_id>/coord')
api.add_resource(new_order, '/delivery/neworder')  # POST REQ




if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=1337)
