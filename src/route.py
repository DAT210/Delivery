import json
import requests

class Route:
    __API_KEY = "AIzaSyA-z2Kd25PFPMs3gCSpC6bzPBazgSWtLGY"
    __API_URL = "https://maps.googleapis.com/maps/api/directions/json?"

    waypoints = {}
    total_duration = 0
    total_distance = 0

    def __init__(self, destination, mode, origin='Sandnes'):
        self.origin = origin
        self.destination = destination
        self.mode = mode

        self.json_directions = self._collect_directions(self.origin, self.destination, self.mode)
        if self._error_check():
            self._init_total_eta_and_distance()
            self._collect_waypoints()
    



    def _collect_waypoints(self):
        self.waypoints = self.json_directions["routes"][0]["legs"][0]["steps"]

    def _collect_directions(self, origin, destination, mode):
        args = "origin={}&destination={}&mode={}&key={}".format(origin, destination, mode, self.__API_KEY)
        data = requests.get(self.__API_URL + args)
        return json.loads(data.content)

    def _init_total_eta_and_distance(self):
        # This can be expanded to allow alternate routes
        self.total_distance = self.json_directions["routes"][0]["legs"][0]["distance"]["value"]/1000  # Convert to KM
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
                