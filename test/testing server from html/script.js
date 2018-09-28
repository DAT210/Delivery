$(document).ready(function() {
    var port = ":4020"
    $("#find").click (function(){
        var containerAddress = "http://" + $('input[name=dockertype]:checked').val() + port
        window.open(containerAddress , '_blank');
    })

    $("#withroute").click (function(){
        var containerAddress = "http://" + $('input[name=dockertype]:checked').val() + port
        window.open(containerAddress+ "/testing" , '_blank');
    })

    $("#routewithget").click (function(){
        var containerAddress = "http://" + $('input[name=dockertype]:checked').val() + port
        var input = $("#theinput1").val()
        window.open(containerAddress+ "/testingget?test="+ input  , '_blank');
    })


});

