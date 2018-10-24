import mysql.connector
import json

class Database:
    def __init__(self, config, g):
        self.db = self.getDB(config, g)
    
    def getDB(self, config, g):
        if not hasattr(g, "_database"):
            g._database = mysql.connector.connect(
                                                user=config["DATABASE_USER"],
                                                password=config["DATABASE_PASSWORD"],
                                                database=config["DATABASE_DB"],
                                                )
        return g._database

    def query(self, sql):
        cur = self.db.cursor()
        try:
            cur.execute(sql)
            row = cur.fetchall()
            return json.dumps(row)
        except mysql.connector.Error:
            return False
        finally:
            cur.close()

    # TODO lage metode for å sette inn timestamps
    # TODO lage metode for å sette inn i delivery
    # TODO lage metode for å sette inn i _address
    # TODO få databasen til å lagre strings i utf8 format
    def query_insert(self):
        cur = self.db.cursor()
        sql = ("INSERT INTO _address VALUES(0, ´Sandnes´, 4326, ´Gamle Austråttvei´, 14, ''")
        try:
            cur.execute(sql)
        except mysql.connector.Error:
            return False
        finally:
            cur.close()

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
                    "street": str(street),  # TODO handle this
                    "street_number": street_number,
                    "house_number": house_number
                })
            return json.dumps(data)
        except mysql.connector.Error:
            return False
        finally:
            cur.close()


        

    



        
