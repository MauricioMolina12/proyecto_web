document.getElementById("loginGO").addEventListener("click", function() {
    window.location.href = "/login";
});



// function saveusuario(){
//      const var_usuario= document.getElementById('userInput').value;
//      const var_email = document.getElementById('emailInput').value;
//      const var_password = document.getElementById('passwordInput').value;
//      const var_confirmarP   = document.getElementById('confirmar').value;

//      var config = {
//          headers: {
//              'Content-Type': 'application/json'
//          }
//      };
//      var data = {
//          nombre: var_usuario,
//          correo: var_email,
//          contraseña: var_password
//      };
//      let usuarioSI = axios.get(`/api/usuarios?nombre=${var_usuario}`)

//          .then(response => {

//              if (usuarioSI !== null) {

//                  alertify.alert('Ya existe un usuario así');

//              }else if(var_password.trim() === var_confirmarP.trim()){
//                  const ruta= 'api/saveusuario'

//                  axios.post(ruta, JSON.stringify(data), config)

//                      .then(function (response) {
//                          var_usuario ="",
//                          var_email ="",
//                          var_password = "",
//                          var_confirmarP = ""

//                          alertify.alert('Datos guardados con exito!');
//                      })
//                      .catch(error => {
//                          alertify.alert('Error al guardar usuario',error);
//                      });
//                  }else{
//                      alertify.alert('Las contraseñas no coinciden');
//                  }
//              })
//              .catch(error => {
//                  console.error('Error al verificar si el usuario existe:', error);
//              });
//  }

//  document.getElementById('btn-r').addEventListener("click",saveusuario());


