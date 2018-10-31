DROP DATABASE IF EXISTS delivery;
CREATE DATABASE delivery CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE delivery;

DROP TABLE IF EXISTS delivery;

CREATE TABLE _address (
    aid INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    city VARCHAR(255) NOT NULL,
    postcode INT(4) NOT NULL,
    street VARCHAR(255) NOT NULL,
    street_number INT(4) NOT NULL,
    house_number CHAR(1)
);

CREATE TABLE delivery (
    did INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    aid INT NOT NULL,
    order_id INT NOT NULL,
    customer_id INT NOT NULL,
    price INT NOT NULL,
    vehicle VARCHAR(255) NOT NULL,
    order_delivered DATETIME,
    order_ready DATETIME,
    FOREIGN KEY (aid) REFERENCES _address(aid)
);

INSERT INTO _address VALUES 
(0, "Sandnes", 4326, "Gamle Austråttvei", 14, '');


