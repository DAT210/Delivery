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

```shell
cd delivery/src
python api.py
python route_tests.py
python delivery_client.py
```

The page for viewing ETA updates will be here: http://localhost:1337/delivery/ORDER_ID/map (replace "ORDER_ID" with the ID of the desired order)


### Building

To run the server and the delivery client first change directory to the src folder of delivery and then execute the api and delivery client:
```shell
cd delivery/src/
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

## Style guide ##TODO

Explain your code style and show how to check it.

##  Api Reference

If the api is external, link to api documentation. If not describe your api including authentication methods as well as explaining all the endpoints with their required parameters.

When the API is running the following endpoints are avaliable:
```
* /delivery/methods/eta
* /delivery/ORDER_ID/eta
* /delivery/neworder
* /delivery/client/update
```
More information on how to send requests is avaliable in the API documentation [here](https://github.com/DAT210/Delivery/blob/dev/docs/deliveryAPI.yaml)

External API's used in this application includes Google's Direction, Geocoder and Maps Javascript API.
Documentation for the different API's can be found below.

[Google Maps Javascript API](https://developers.google.com/maps/documentation/javascript/tutorial)
[Google Directions API](https://developers.google.com/maps/documentation/directions/start)
[Google Geocoding API](https://developers.google.com/maps/documentation/geocoding/start)


https://developers.google.com/maps/documentation/directions/start
## Database ##TODO

Explaining what database (and version) has been used. Provide download links.
Documents your database design and schemas, relations etc... 

## Licensing ##TODO

State what the license is and how to find the text version of the license.
