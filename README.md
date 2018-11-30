[![Build Status](https://dev.azure.com/dat210h18/DAT210/_apis/build/status/DAT210.Delivery)](https://dev.azure.com/dat210h18/DAT210/_build/latest?definitionId=11)
![Logo of the project](https://bigmickey.ie/wp-content/uploads/2017/10/Delivery.png)

# Delivery [![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](https://github.com/your/your-project/blob/master/LICENSE)

> Delivery service for restaurant project

Delivery service that will provide APIs for obtaining info regarding available delivery options, ETAs and tracking for customers.

## Installing / Getting started
```shell
git clone https://github.com/DAT210/Delivery.git
cd to repo directory
run command: "docker-compose up --build"
```

### Container should now be visible
* On docker: localhost:22000
* On docker toolbox: 192.168.99.100:22000

## Developing

### Built With
* [Python 3](https://www.python.org/download/releases/3.0/)
* [Flask](http://flask.pocoo.org/)
* [MySQL](https://www.mysql.com/)
* [Docker](https://www.docker.com/get-started)

### Prerequisites
* [Python 3](https://www.python.org/download/releases/3.0/)
* [Flask](http://flask.pocoo.org/)
* [MySQL](https://www.mysql.com/)
* [Docker](https://www.docker.com/get-started)


### Setting up Development environment

For further development the developer needs to have [Python 3](https://www.python.org/download/releases/3.0/) installed. The easiest way to get Pyhton 3 as well as a ot of frequently used packages is by installing [Anaconda](https://www.anaconda.com/download/).

When all is set up clone the repository with the command below.
```shell
git clone https://github.com/DAT210/Delivery.git
```

If you install a clean version of Python 3 you also have to install these packages from commandline.
```shell
pip install flask
pip install mysql-connector
pip install requests
```

### Run and test the newly set up environment
The purpose of this API is to update ETA for a delivery. It's reliant on a service to provide GPS coordinates to continously update ETA and position.
To do this there is an avaliable script to simulate this, as well as a script to create fake orders.


To start the simulation, run the server trough docker and run the order generator script that resides in src/client/route_tests.py. You have to secify the target URL here depending on you are running in Docker Toolbox or Docker.


The page for viewing ETA updates will be here: http://localhost:1337/delivery/ORDER_ID/map (replace "ORDER_ID" with the ID of the desired order)



### Building without Docker

To run the server and the delivery client without Docker first change directory to the src folder of delivery and then execute the api and then the delivery client which resides in src/client:
```shell
cd delivery/src/
python api.py
cd /client
python delivery_client.py
```

The api should now be available on http://localhost:1337


### Deployin
There is an Azure pipeline that automaticly builds the two containers running the API and delivery client. This pipe rebuilds automaticly every time there is a new commit to the master branch. 

This means you dont have to do anything, unless you have made changes regarding containers. (Added, removed, edited).

## Versioning

We use [SemVer](http://semver.org/) for versioning. That means the MAJOR.MINOR.PATCH notation.

The application is currently in version 1.0.0

## Configuration

If the user wants to run the full application on their own computer, you might have to alter the request URL in the route_tests.py script which resides in Delivery/src/client. The target adress will vary depending on you run the application from commandline, Docker or Docker Toolbox.

## Tests

Tests against the API is written in postman and you will therefore need [Postman](https://www.getpostman.com/) to run these tests. One alternative is to use Newman which buids on Node.js and run the tests from commandline.

The tests is saved under: 
```
delivery/test/integration/Delivery_API_tests.json
```

Load this file in to Postman and you will get a collection with tests that can test all thh API methods, both in legan and illegal ways. These tests can be run together as a collection or seperatly.


### Python

* Follow PEP8

### Javascript

* Four space indentation

* Single quotes are preferred

* Use '===' insted of '==' in comparison
```javascript
// no
if (5 == '5') {
    ...
}

// yes
if (5 === '5') {
    ...
}

```

### HTML

* Four space indentation


##  Api Reference

If the api is external, link to api documentation. If not describe your api including authentication methods as well as explaining all the endpoints with their required parameters.

When the API is running the following endpoints are avaliable:

```shell
 /delivery/methods/eta
 /delivery/ORDER_ID/eta
 /delivery/neworder
 /delivery/client/update
```
More information on how to send requests is avaliable in the API documentation [here](https://github.com/DAT210/Delivery/blob/dev/docs/deliveryAPI.yaml)

External API's used in this application includes Google's Direction, Geocoder and Maps Javascript API.
Documentation for the different API's can be found below.

[Google Maps Javascript API](https://developers.google.com/maps/documentation/javascript/tutorial)

[Google Directions API](https://developers.google.com/maps/documentation/directions/start)

[Google Geocoding API](https://developers.google.com/maps/documentation/geocoding/start)


## Database

For our application we used MySQL (version 5.7), but dependencies are automatically downloaded when using Docker. 

We have used the python/mysql-connector for this appication, see documentation for that here [here](https://dev.mysql.com/doc/connectors/en/connector-python.html) and some code examples are available [here](https://dev.mysql.com/doc/connectors/en/connector-python-examples.html)

Download MySQL [here](https://dev.mysql.com/downloads/mysql/) (Available for all popular operation systems Windows, MacOS, Linux etc.)

We use the following schema for out database:

### Address table

|Field         |Type          | Null         |Key           |Default       |Extra         |
|--------------|--------------|--------------|--------------|--------------|--------------|
|aid           |int(11)       |NO            |PRI           |NULL          |auto_increment|
|city          |varchar(255)  |NO            |              |NULL          |              |
|postcode      |int(4)        |NO            |              |NULL          |              |
|street        |varchar(255)  |NO            |              |NULL          |              |
|street_number |int(4)        |NO            |              |NULL          |              |
|house_number  |char(1)       |YES           |              |NULL          |              |

### Transport table

|Field          |Type           | Null          |Key            |Default        |Extra          |
|---------------|---------------|---------------|---------------|---------------|---------------|
|tid            |int(11)        |NO             |PRI            |NULL           |auto_increment|
|aid            |int(11)        |NO             |MUL            |NULL           |              |
|order_id       |int(11)        |NO             |               |NULL           |              |
|customer_id    |int(11)        |NO             |               |NULL           |              |
|price          |int(11)        |NO             |               |NULL           |              |
|vehicle        |varchar(255)   |NO             |               |NULL           |              |
|order_delivered|datetime       |YES            |               |NULL           |              |
|order_ready    |datetime       |YES            |               |NULL           |              |

### Design Reasoning

We have desided to normalize our database in order manily to avoid storing
replicated data, but also to avoid anomalies.
We have separated the tables into transport and address, separating the data associated with each relevant into each table.
The transport table holds a foreign key to the address table creating a relationship where an address can have multiple transports.

This practicaly means that we can allow a customer to have mulitple orders
delivered to the same address.

## Licensing 

MIT License

Copyright (c) Asle Berge, Ole Joar Moi and Mads Andersson

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
