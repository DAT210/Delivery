import requests, json

class Geocoder:
    __API_KEY = "AIzaSyCuIwZpGcrFtXgGk_rk4MJeW7Musdj9Jm8"
    __API_URL = "https://maps.googleapis.com/maps/api/geocode/json?"

    def __init__(self, address):
        self.address = address
        self.lat, self.lng = self._geocode_address()



    def _geocode_address(self):
        payload = {"address": self.address, "key": self.__API_KEY}

        data = requests.get(self.__API_URL + "key={}&address={}".format(payload["key"], payload["address"]))
        json_data = json.loads(data.content)
        lat, lng = json_data["results"][0]["geometry"]["location"]["lat"], json_data["results"][0]["geometry"]["location"]["lng"]
        return lat,lng