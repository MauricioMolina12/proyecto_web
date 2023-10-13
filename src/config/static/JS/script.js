document.getElementById("loginGO").addEventListener("click", function() {
    window.location.href = "/login";
});



const registroBtn = document.querySelector('.btn');

registroBtn.addEventListener('click', () => {
    const username = document.querySelector('input[name="user"]');
    const email = document.querySelector('input[name="email"]');
    const password = document.querySelector('input[name="passwordInput"]');
    const confirmPasswordInput = document.querySelector('input[name="Cpassword"]');

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

function postUser(username, email, password) {
    let options = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "User-Agent": "insomnia/8.1.0",
      },
      body:
        '{"username":"' +
        username +
        '","email":"' +
        email +
        '","password":"' +
        password +
        '"}',
    };
  
    fetch("http://localhost:5000/api/saveusuario", options)
      .then((response) => response.json())
      .then((response) => console.log(response))
      .catch((err) => console.error(err));
  }