DROP DATABASE IF EXISTS testdb;
CREATE DATABASE testdb;
USE testdb;

DROP TABLE IF EXISTS transport;

CREATE TABLE transport (
    tid INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    vehicle VARCHAR(255) NOT NULL,
    ETA INT
);

INSERT INTO transport VALUES 
(1, "BIKE", 40),
(2, "BIKE", 45),
(3, "TAXI", 20),
(4, "HELICOPTER", 10),
(5, "DRONE", 15),
(6, "TAXI", 20),
(7, "DRONE", 15);


