
document.getElementById("signup").addEventListener("click", function() {
    window.location.href = "/register";
});

document.getElementById("signin").addEventListener("click", function() {
    window.location.href = "/login";
});


function iniciarMap(){
    var coord = {lat:10.9811017 ,lng: -74.7837371};
    var map = new google.maps.Map(document.getElementById('map'),{
      zoom: 12,
      center: coord
    });
    var marker = new google.maps.Marker({
      position: coord,
      map: map
    });
}   