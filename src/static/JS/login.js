document.getElementById("RegisterGO").addEventListener("click", function() {
    window.location.href = "/register";
});

 const usuarioInput = document.querySelector('input[name="user"]');
 const emailInput = document.querySelector('input[name="email"]');
 const passwordInput = document.querySelector('input[name="password"]');
 const confirmPasswordInput = document.querySelector('input[name="Cpassword"]');

 const registroBtn = document.querySelector('.btn');

 registroBtn.addEventListener('click', () => {
     const nombre = usuarioInput.value;
     const correo = emailInput.value;
     const contraseña = passwordInput.value;
     const confirmarContraseña = confirmPasswordInput.value;

     axios.post('/saveusuario', {
         nombre: nombre,
         correo: correo,
         contraseña: contraseña
     })
     .then(function (response) {
         console.log(response.data);
     })
     .catch(function (error) {
         console.error(error);
     });
 });