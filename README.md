![Logo of the project](https://bigmickey.ie/wp-content/uploads/2017/10/Delivery.png)

# Delivery - Group 2

> Delivery service for restaurant project

Delivery service that will provide APIs for obtaining info regarding available delivery options and ETAs.

## Installing / Getting started
```shell
git clone https://github.com/DAT210/Delivery.git
cd to repo directory
run command: "docker-compose up --build"
```

### Container should now be visible
* On docker: localhost:4020
* On docker toolbox: 192.168.99.100:4020

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

The purpose of this API is to update ETA for a delivery. It's reliant on a service to provide GPS coordinates to continously update ETA and position.
To do this there is an avaliable script to simulate this, as well as a script to create fake orders.


To start the simulation, run the server, order generator script and the delivery client.


The page for viewing ETA updates will be here: http://localhost:1337/delivery/ORDER_ID/map (replace "ORDER_ID" with the ID of the desired order)



### Building

To run the server and the delivery client first change directory to the src folder of delivery and then execute the api and delivery client:
```shell
cd delivery/src/
```

```python
python api.py
python delivery_client.py
```

The api should now be available on http://localhost:1337

### Deploying / Publishing ##TODO
give instructions on how to build and release a new version
In case there's some step you have to take that publishes this project to a
server, this is the right time to state it.

```shell
packagemanager deploy your-project -s server.com -u username -p password
```

And again you'd need to tell what the previous code actually does.

## Versioning ##TODO

We can maybe use [SemVer](http://semver.org/) for versioning. For the versions available, see the [link to tags on this repository](/tags).

## Configuration ##TODO

Here you should write what are all of the configurations a user can enter when
using the project.

## Tests

Tests against the API is written in postman and you will therefore need [Postman](https://www.getpostman.com/) to run these tests. One alternative is to use Newman which buids on Node.js and run the tests from commandline.

The tests is saved under: 
```
delivery/test/integration/Delivery_API_tests.json
```

Load this file in to Postman and you will get a collection with tests that can test alle teh API methods, both in legan and illegal ways. These tests can be run together as a collection or seperatly.

## Style guide

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
