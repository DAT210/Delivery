
$(Document).ready(function() {
    var geocoder = new google.maps.Geocoder();
    var start_address = "Gauselarmen 14";
    // var end_address = "Gamle austråttvei 14";
    
    geocodeAddress(geocoder, start_address, function(latlng){
            var map = new google.maps.Map(document.getElementById("map"), 
            {
                center: {lat: latlng[0], lng: latlng[1]},
                zoom: 10
            });
            var pointA = new google.maps.Marker(
            {
                position: { lat: latlng[0], lng: latlng[1] },
                map: map
            });
    });
});


function geocodeAddress(geocoder, address, callback) {
    var latlng = Array(2);
    geocoder.geocode({ "address": address }, function (results, status) {
        if (status === "OK") {
            latlng[0] = results[0].geometry.location.lat();
            latlng[1] = results[0].geometry.location.lng();
            callback(latlng)
        } else {
            alert('Geocode was not successful for the following reason: ' + status);
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


// function calculateAndDisplayRoute(directionsService, directionsDisplay, start, end) {
//     directionsService.route({
//         origin: start,
//         destination: end,
//         travelMode: google.maps.TravelMode.DRIVING
//     }, function (response, status) {
//         if (status == google.maps.DirectionsStatus.OK) {
//             directionsDisplay.setDirections(response);
//         } else {
//             window.alert('Directions request failed due to ' + status);
//         }
//     });
// }
