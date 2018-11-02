import json
import requests

class Route:
    __API_KEY = "AIzaSyA-z2Kd25PFPMs3gCSpC6bzPBazgSWtLGY"
    __API_URL = "https://maps.googleapis.com/maps/api/directions/json?"

    waypoints = {}
    total_duration = 0
    total_distance = 0
    total_price = 0

    def __init__(self, destination, mode, origin='Sandnes'):
        self.origin = origin
        self.destination = destination
        self.mode = mode

        self.json_directions = self._collect_directions(self.origin, self.destination, self.mode)
        if self._error_check():
            self._init_total_eta_and_distance()
            self._collect_waypoints()
            self._calculate_price()
    



    def _collect_waypoints(self):
        self.waypoints = self.json_directions["routes"][0]["legs"][0]["steps"]

    def _collect_directions(self, origin, destination, mode):
        payload = {"origin": origin, "destination", destination, "mode": mode, "key": self.__API_KEY}

        if origin["lat"]:
            payload["origin"] = "{},{}".format(origin["lat"], origin["long"])

        data = requests.get(self.__API_URL, params=payload)
        return json.loads(data.content)

    def _init_total_eta_and_distance(self):
        # This can be expanded to allow alternate routes
        self.total_distance = self.json_directions["routes"][0]["legs"][0]["distance"]["value"]/1000  # Convert to KM
        if self.total_distance > 30:
            raise ValueError("Can't deliver over 30 km")
        self.total_duration = self.json_directions["routes"][0]["legs"][0]["duration"]["value"]/60  # Convert to minutes

    
    def _error_check(self):
        if self.destination == "" or self.destination == None:
            raise ValueError("Destination address is empty.")

        if self.origin == "" or self.origin == None:
            raise ValueError("Origin address is empty.")

        for waypoint in self.json_directions["geocoded_waypoints"]:
            if waypoint["geocoder_status"] != "OK":
                raise ValueError("Address is not valid: {}".format(waypoint["geocoder_status"]))

        return True


    def _calculate_price(self):
        price_base = {
            "driving": {
                "start_price": 30,
                "time_price": 175,
                "km_price": 4
            },
            "walking": {
                "start_price": 15,
                "time_price": 150,
                "km_price": 40
            },
            "transit": {
                "start_price": 20,
                "time_price": 150,
                "km_price": 10
            }
        }

        start_price = price_base[self.mode]["start_price"]
        time_price = price_base[self.mode]["time_price"]
        km_price = price_base[self.mode]["km_price"]

        self.total_price = start_price + time_price*(self.total_duration/60) + km_price*self.total_distance


        

                