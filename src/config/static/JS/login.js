document.getElementById("RegisterGO").addEventListener("click", function() {
    window.location.href = "/register";
});

// function loginUsuario(){
//     let var_usuario = document.getElementById('userInput').value
//     let var_password = document.getElementById('passwordInputInput').value

//     axios.get(`api/usuarios?nombre=${var_usuario}&contraseña=${var_password}`)
//     .then(response =>{
//         if(response.data){
//             window.location.href("/map");
//         }else{
//             alertify.alert('Credenciales incorrectas');
//         }
//     })
//     .catch(error => {
//         // La solicitud falló, maneja el error aquí
//         console.error(error);
//     });
// }