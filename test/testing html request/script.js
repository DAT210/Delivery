$(document).ready(function() {
    var port = ":4020"
    $("#find").click (function(){
        var containerAddress = "http://" + $('input[name=dockertype]:checked').val() + port;
        window.open(containerAddress , '_blank');
    })

    $("#withroute").click (function(){
        var containerAddress = "http://" + $('input[name=dockertype]:checked').val() + port;
        window.open(containerAddress+ "/testing" , '_blank');
    })

    $("#routewithget").click (function(){
        var containerAddress = "http://" + $('input[name=dockertype]:checked').val() + port;
        var input = $("#theinput1").val();
        window.open(containerAddress+ "/testingget?test="+ input  , '_blank');
    })

    $("#routewithpost").click (function(){
        var containerAddress = "http://" + $('input[name=dockertype]:checked').val() + port;
        var input = $("#theinput2").val();
        console.log(containerAddress)
        $("#routewithpostform").submit(testPOST(containerAddress, "/testingpost", $('#routewithpostform').serialize()));
    })


});
function testPOST(containerAddress, path, indata){
    $.ajax({
        url: containerAddress+path,
        type: 'POST',
        data : indata,
        success: function(data){
            var w = window.open('','_blank');
                w.document.open();
                w.document.write(data);
                w.document.close();
        }
    });
}