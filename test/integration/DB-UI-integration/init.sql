DROP DATABASE IF EXISTS testdb;
CREATE DATABASE testdb;
USE testdb;

DROP TABLE IF EXISTS transport;

CREATE TABLE transport (
    tid INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    vehicle VARCHAR(255) NOT NULL,
    _time DATETIME,
    city VARCHAR(255) NOT NULL,
    postcode INT(4) NOT NULL,
    street VARCHAR(255) NOT NULL,
    street_number INT NOT NULL
);

INSERT INTO transport VALUES 
(0, "BIKE", CURRENT_TIMESTAMP, "Sandnes", 4326, "Gamle austråttvei", 14),
(0, "TAXI", CURRENT_TIMESTAMP, "Stavanger", 4032, "Gauselarmen", 14),
(0, "TAXI", CURRENT_TIMESTAMP, "Stavanger", 4032, "Gauselarmen", 12),
(0, "TAXI", CURRENT_TIMESTAMP, "Stavanger", 4032, "Gauselarmen", 11);


