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
        // path = /delivery/<order_id>/map
        var url = window.location.pathname;
        var id = url.split("/")[2];
        $.ajax({
            type: "GET",
            url: "/delivery/" + id + "/eta",
            dataType: "json",
            success: function (response) {
                var markerLat = (markers[markers.length - 1]).getPosition().lat().toFixed(6);
                var markerLng = (markers[markers.length - 1]).getPosition().lng().toFixed(6);
                var responseLat = response.lat.toFixed(6);
                var responseLng = response.lng.toFixed(6);
                if (markerLat === responseLat && markerLng == responseLng){
                    console.log("markers have the same position")
                }else{
                    setNewMarker(response.lat, response.lng)
                }
                
            },
            error: function (error) {
            alert("something went wrong (GET)")
            console.log(error)
            }
        });
    }, 2000);

});

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
    for (i=0 ; i < markers.length-1 ; i++) {
        markers[i].setMap(null);
    }
}


function setNewMarker(lat, lng){
    var latlng = new google.maps.LatLng(lat, lng);
    searchResults.push(latlng)
    var marker = new google.maps.Marker({
        map: map,
        position: latlng,
    });

    markers.push(marker);
    removePrevMarker();
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
