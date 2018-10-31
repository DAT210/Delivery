var geoResults = {};
var geocoder;
var map;
var searchResults = [];
var markers = [];
var startAddr = "Gauselarmen 14";
var endAddr = "Gamle austråttvei 14";
var directionsDisplay;
var directionsService;


$(function(){
    setInterval(function () {
        var url = window.location.pathname;
        var id = url.substring(url.lastIndexOf('/') + 1);
        $.ajax({
            type: "GET",
            url: "/delivery/eta/" + id,
            dataType: "json",
            success: function (response) {
                setNewMarker(response.lat, response.lng);
            },
            error: function (error) {
            alert("something went wrong (GET)")
            console.log(error)
            }
        });
    }, 5000);

});

// icons: https://icons8.com

function initMap() {
    geocoder = new google.maps.Geocoder();
    var latlng = new google.maps.LatLng(-34.397, 150.644)
    var myOptions = {
        zoom: 8,
        center: latlng,
    }
    map = new google.maps.Map(document.getElementById('map'), myOptions);
    // geocodeAddress(startAddr);
    geocodeAddress(endAddr);
}

function removePrevMarker() {
    for (i=0 ; i<markers.length-1 ; i++) {
        markers[i].setMap(null);
    }
}

// TODO: finne ut hvordan man sette inn et custom icon
// fikse slik at den første også blir et icon
// fikse slik at destinasjonsadressen er et målflagg og ikke flytter på seg

var markerIcon = {
    url: 'car.svg',
    scaledSize: new google.maps.Size(60, 60),
    origin: new google.maps.Point(0, 0), // used if icon is a part of sprite, indicates image position in sprite
    anchor: new google.maps.Point(20, 40) // lets offset the marker image
};

function setNewMarker(lat, lng){
    // var image = "http://image.flaticon.com/icons/svg/252/252025.svg"
    var latlng = new google.maps.LatLng(lat, lng);
    searchResults.push(latlng)
    var marker = new google.maps.Marker({
        icon: markerIcon,
        map: map,
        position: latlng,
    });
    markers.push(marker);
    console.log(markers.length)
    removePrevMarker();

    // console.log(markers.length)
    // if (markers.length >= 2) {
    //     directionsService = new google.maps.DirectionsService();
    //     directionsDisplay = new google.maps.DirectionsRenderer();
    //     directionsDisplay.setMap(map);
    //     calculateAndDisplayRoute(directionsService, directionsDisplay);
    // }
}

function geocodeAddress(address) {
    geocoder.geocode({ "address": address }, function (results, status) {
        if (status === "OK") {
            map.setCenter(results[0].geometry.location);
            var marker = new google.maps.Marker({
                map: map,
                position: results[0].geometry.location
            });
            searchResults.push(results[0].geometry.location);
            console.log(results[0].geometry.location);
            markers.push(marker);
        }else {
            alert("Geocode was not successful for the following reason: " + status);
        }
    });
}

// function calculateAndDisplayRoute(directionsService, directionsDisplay) {
//     directionsService.route({
//         origin: searchResults[1],
//         destination: searchResults[0],
//         travelMode: google.maps.TravelMode.DRIVING
//     }, function (response, status) {
//         if (status == google.maps.DirectionsStatus.OK) {
//             directionsDisplay.setDirections(response);
//         } else {
//             window.alert('Directions request failed due to ' + status);
//         }
//     });
// }
