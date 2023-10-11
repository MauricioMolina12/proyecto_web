
document.getElementById("signup").addEventListener("click", function() {
    window.location.href = "/register";
});

document.getElementById("signin").addEventListener("click", function() {
    window.location.href = "/login";
});

var botonRoute = document.getElementById("route");

botonRoute.addEventListener("click", function(event) {
    event.preventDefault();

    var opcionesVentana = "width=300,height=300,toolbar=no,location=no,status=no,menubar=no,scrollbars=no,resizable=yes";

    var left = (window.innerWidth - 280) / 2;
    var top = (window.innerHeight - 150) / 2;
    
    var chooseroute = window.open("", "VentanaEmergente", opcionesVentana + ",left=" + left + ",top=" + top);
    

    // Contenido de la ventana emergente
    var contenidoVentana = `
        <html>
        <head>
            <title>RutaSegura</title>
            <style>
                body {
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    flex-direction: column;
                    background-color: #3D3E3C;
                    color: white;
                    font-family: 'Arimo', sans-serif;
                    text-align: center;
                    margin: 0;
                    padding: 20px;
                }
                h1 {
                    font-family: 'Righteous';
                }
                .boton {
                    background-color: #5DB7DE;
                    color: white;
                    padding: 10px 20px;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                    margin-top: 20px;
                }
            </style>
        </head>
        <body>
            <h1>¿Qué deseas hacer?</h1>
            <button id="proponer" class="boton">Proponer nueva ruta</button>
            <button id="mostrar" class="boton">Mirar rutas existentes</button>
        </body>
        </html>
    `;

    // Escribe el contenido en la ventana emergente
    chooseroute.document.write(contenidoVentana);
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