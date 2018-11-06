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
                // hvordan sette status.order?
                // hvordan sette statusbaren?
                var status = response.status;
                var eta = response.eta.current.val;
                var totalTime = response.eta.total.val;
                var markerLat = (markers[markers.length - 1]).getPosition().lat().toFixed(6);
                var markerLng = (markers[markers.length - 1]).getPosition().lng().toFixed(6);
                var responseLat = parseFloat(response.lat).toFixed(6);
                var responseLng = parseFloat(response.lng).toFixed(6);
                var percent = parseInt((1 - (eta / totalTime)) * 100)
                console.log(percent)
                $('#msg').css("display", "block").html("status: " + status)
                $('#prog-bar').css("width", percent + "%");
                $('#progress-text').html(percent + "%")
                if (markerLat === responseLat && markerLng == responseLng){
                    console.log("markers have the same position")
                }else{
                    setNewMarker(response.lat, response.lng)
                }
                
            },
            error: function (error) {
            console.log("1. something went wrong (GET)");
            console.log(error);
            }
        });
    }, 5000);

    // {
    //     "eta": {
    //         "current": {
    //             "text": "9 minutes",
    //                 "val": 540
    //         },
    //         "total": {
    //             "text": "13 minutes",
    //                 "val": 780
    //         }
    //     },
    //     "final_destination": "gausel+armen+23+stavanger",
    //         "lat": "58.8564518",
    //             "long": "5.7133463",
    //                 "status": "None"
    // }
});



function initMap() {
    geocoder = new google.maps.Geocoder();
    var latlng = new google.maps.LatLng(-34.397, 150.644);
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
    searchResults.push(latlng);
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
