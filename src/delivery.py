import geocoder

class Delivery:

    def __init__(self, delivery_method, destination, order_id, status, route, origin="Sandnes", eta=None):
        self.delivery_method = delivery_method
        self.destination = destination
        self.status = status
        self.order_id = order_id
        self.origin = origin
        self.destination_coord = self._get_coordinates(destination)
        self.origin_coord = self._get_coordinates(origin)
        self.route = route

    def _get_coordinates(self, address):
        geo = geocoder.Geocoder(address)
        return {"lat": geo.lat, "long": geo.lng}

