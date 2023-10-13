document.getElementById("loginGO").addEventListener("click", function() {
    window.location.href = "/login";
});



const registroBtn = document.querySelector('.btn');

registroBtn.addEventListener('click', () => {
    const username = document.querySelector('input[name="user"]');
    const email = document.querySelector('input[name="email"]');
    const password = document.querySelector('input[name="passwordInput"]');
    const confirmPasswordInput = document.querySelector('input[name="Cpassword"]');

    if (password == confirmPasswordInput):
        alert('Las contraseñas no coinciden')
};
  

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