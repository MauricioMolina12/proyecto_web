
document.getElementById("signup").addEventListener("click", function() {
    window.location.href = "/register";
});

document.getElementById("signin").addEventListener("click", function() {
    window.location.href = "/login";
});



// function iniciarMap(){
//     var coord = {lat:10.9811017 ,lng: -74.7837371};
//     var map = new google.maps.Map(document.getElementById('map'),{
//       zoom: 12,
//       center: coord
//     });
//     var marker = new google.maps.Marker({
//       position: coord,
//       map: map
//     });
// }   

let map;

async function initMap() {
  const { Map } = await google.maps.importLibrary("maps");
  var coord = {lat:10.9811017 ,lng: -74.7837371};
  map = new google.maps.Map(document.getElementById("map"), {
    center: coord,
    zoom: 12,
  });
  var marker = new google.maps.Marker({
    position: coord,
    map: map
  });
}

initMap();