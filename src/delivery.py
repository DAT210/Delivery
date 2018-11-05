

class Delivery:

    def __init__(self, delivery_method, destination, order_id, status, route, origin=None, eta=None):
        self.delivery_method = delivery_method
        self.destination = destination
        self.order_id = order_id
        self.status = status
        self.route = route

        if origin:
            self.origin = origin

        self._insert_to_db()


        


    def _insert_to_db(self):
        return