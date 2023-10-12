document.getElementById("loginGO").addEventListener("click", function() {
    window.location.href = "/login";
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

    if (!nombre || !correo || !contraseña || !confirmarContraseña) {
        alert('No ha completado la información en los campos.');
        return;
    }

    if (contraseña !== confirmarContraseña) {
        alert('Las contraseñas no coinciden.');
        return;
    }
   

    // axios.post('http://localhost:5000/api/saveusuario', {
    //     nombre: nombre,
    //     correo: correo,
    //     contraseña: contraseña
    // })
    // .then(function (response) {
    //     console.log(response.data);
    // })
    // .catch(function (error) {
    //     console.error(error);
    //     alert('Error al registrar usuario.');
    // });
});

