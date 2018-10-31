import json, requests, time

NAMES = ["Karl", "Per", "Knut", "Ole J Moi", "Asle Berge"]
URL_GET_JOBS = "http://127.0.0.1:1337/delivery/client/job?"
URL_SEND_UPDATE = "http://127.0.0.1:1337/delivery/client/update?"


def main():
    delivery_clients = []

    for name in NAMES:
        delivery_clients.append(Delivery_client(name))
    
    while True:
        print("\nChecking status for eache deliveryman on job\n----------------------------------")    
        for client in delivery_clients:
            if client.job == None:
                if client._get_job():
                    print("{} have taken and started delivery on job nr {}".format(client.name, client.job["order_id"]))
                    client._start_leg()
                else:
                    print("No job available for {}".format(client.name))
            else:
                print("{} alreeady has a job assigned. Checking status.".format(client.name))
                client._check_progress()
        time.sleep(5)
        

    
        

class Delivery_client:
    legs = []
    leg_start_time = None
    start_time = None

    def __init__(self, name):
        self.name = name
        self.job = None
        self.leg = None


    #Checks if the client have a delivery job
    def _have_job(self):
        if self.job == None:
            return False
        return True

    #Fetches a new job for the client
    def _get_job(self):
        r = requests.get(URL_GET_JOBS).content
        if json.loads(r) == "No jobs available":
            return False
        else:
            self.job = json.loads(r)
            for legs in self.job["legs"]:
                self.legs.append(legs)
                self.leg = 0
            return True
    
    #Starts simulation of the delivery
    def _start_leg(self):
        self.start_time = time.time()
        self.leg_start_time = time.time()
        requests.get(URL_SEND_UPDATE + "order={}&lat={}&lng={}".format(self.job["order_id"], self.job["legs"][self.leg]["latitude"], self.job["legs"][self.leg]["latitude"]))

    #Checks for progress in the delivery
    def _check_progress(self):
        time_gone = time.time() - self.leg_start_time
        if time_gone < self.legs[self.leg]["time"]:
            print("{} is still in leg {} of {}. Time left: {}".format(self.name, self.leg + 1, len(self.legs), self.legs[self.leg]["time"]-time_gone))
        elif self.legs[self.leg + 1]["time"] == 0:
            print("{} is finished with the delivery. Will look for new. Delivered in {} seconds.".format(self.name, time.time()-self.start_time))
            requests.get(URL_SEND_UPDATE + "order={}&lat={}&lng={}".format(self.job["order_id"], self.job["legs"][self.leg]["latitude"], self.job["legs"][self.leg]["latitude"]))
            self.job = None
            self.leg_start_time = None
            self.start_time = None
            self.leg = 0
        else:
            self.leg = self.leg + 1
            self.leg_start_time = time.time()
            print("{} is now in leg {} of {}".format(self.name, self.leg, len(self.legs)))
            requests.get(URL_SEND_UPDATE + "order={}&lat={}&lng={}".format(self.job["order_id"], self.job["legs"][self.leg]["latitude"], self.job["legs"][self.leg]["latitude"]))
    

if __name__ == '__main__':
    main()

