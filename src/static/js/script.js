var geoResults = {};
var geocoder;
var map;
var searchResults = [];
var startAddr = "Gauselarmen 14";
var endAddr = "Gamle austråttvei 14";
var directionsDisplay;
var directionsService = new google.maps.DirectionsService();

function initMap() {
    directionsService = new google.maps.DirectionsService();
    directionsDisplay = new google.maps.DirectionsRenderer();
    geocoder = new google.maps.Geocoder();
    var latlng = new google.maps.LatLng(-34.397, 150.644)
    var myOptions = {
        zoom: 8,
        center: latlng,
    }
    map = new google.maps.Map(document.getElementById('map'), myOptions);
    directionsDisplay.setMap(map);
    geocodeAddress(startAddr);
    geocodeAddress(endAddr);
    console.log(searchResults)

}

function geocodeAddress(address) {
    geocoder.geocode({ "address": address }, function (results, status) {
        if (status === "OK") {
            map.setCenter(results[0].geometry.location);
            var marker = new google.maps.Marker({
                map: map,
                position: results[0].geometry.location
            });

            searchResults[address] = results[0].geometry.location;
        }else {
            alert("Geocode was not successful for the following reason: " + status);
        }
    });
}

function calculateAndDisplayRoute(directionsService, directionsDisplay) {
    console.log(searchResults)
    console.log(searchResults.startAddr)
    directionsService.route({
        origin: searchResults[startAddr],
        destination: searchResults[endAddr],
        travelMode: google.maps.TravelMode.DRIVING
    }, function (response, status) {
        if (status == google.maps.DirectionsStatus.OK) {
            directionsDisplay.setDirections(response);
        } else {
            window.alert('Directions request failed due to ' + status);
        }
    });
}











    // map = new google.maps.Map(
    //     document.getElementById('map'),
    //     {
    //         zoom: 4,
    //         center: start_location
    //     });
    // var marker = new google.maps.Marker(
    //     {
    //         position: start_location,
    //         map: map
    //     });


    //     zoom: 8,
    //     center: { lat: -34.394, lng: 150.644 },
    //     // Instantiate a directions service.
    //     directionsService = new google.maps.DirectionsService,
    //     directionsDisplay = new google.maps.DirectionsRenderer({
    //         map: map,

    // get route from start to end
    // calculateAndDisplayRoute(directionsService, directionsDisplay, start, end)

