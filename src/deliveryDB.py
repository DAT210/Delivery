import mysql.connector
import json
from flask import g


# config refers to the app.config dict
class Database:
    def __init__(self, config):
        self.db = self.getDB(config)
    
    def getDB(self, config):
        if not hasattr(g, "_database"):
            g._database = mysql.connector.connect(
                                                user=config["DATABASE_USER"],
                                                password=config["DATABASE_PASSWORD"],
                                                database=config["DATABASE_DB"],
                                                )
        return g._database

    # TODO få databasen til å lagre strings i utf8 format FAAACCCCKKK!!!
    # TODO kjør tester

    # 1. method: Fetch all from first table (delivery)
    def query_delivery(self):
        cur = self.db.cursor()
        sql = "SELECT did, aid, order_id, customer_id, price, vehicle, order_delivered, order_ready FROM delivery"
        try:
            cur.execute(sql)
            data = []
            for did, aid, order_id, customer_id, price, vehicle, order_delivered, order_ready in cur:
                data.append({
                    "did": did,
                    "aid": aid,
                    "order_id": order_id,
                    "customer_id": customer_id,
                    "price": price,
                    "vehicle": vehicle,
                    "order_delivered": order_delivered,
                    "order_ready": order_ready
                })
            return json.dumps(data)
        except mysql.connector.Error:
            return False
        finally:
            cur.close()

    # 2. fetch all from (_address)
    def query_address(self):
        cur = self.db.cursor()
        sql = "SELECT aid, city, postcode, street, street_number, house_number FROM _address"
        try:
            cur.execute(sql)
            data = []
            for aid, city, postcode, street, street_number, house_number in cur:
                data.append({
                    "aid": aid,
                    "city": city,
                    "postcode": postcode,
                    "street": str(street),
                    "street_number": street_number,
                    "house_number": house_number
                })
            return json.dumps(data)
        except mysql.connector.Error:
            return False
        finally:
            cur.close()

    # 3. method insert into delivery
    # pass inn ann array containing all eight fields
    def insert_delivery(self, data):
        cur = self.db.cursor()
        sql = "INSERT INTO delivery VALUES ({}, {}, {}, {}, {}, {}, {}, {})" \
        .format(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7])
        try:
            cur.execute(sql)
            return True
        except mysql.connector.Error:
            return False
        finally:
            cur.close()

    # 4. method insert into delivery
    # pass inn ann array containing all six fields
    def insert_address(self, data):
        cur = self.db.cursor()
        sql = "INSERT INTO _address VALUES ({}, {}, {}, {}, {}, {})" \
            .format(data[0], data[1], data[2], data[3], data[4], data[5])
        try:
            cur.execute(sql)
            return True
        except mysql.connector.Error:
            return False
        finally:
            cur.close()

        

    



        
