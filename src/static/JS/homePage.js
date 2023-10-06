document.getElementById("sigup").addEventListener("click", function() {
    window.location.href = "Register.html";
});

document.getElementById("signin").addEventListener("click", function() {
    window.location.href = "Login.html";
});


const mobileMenuButton = document.getElementById('mobile-menu');
const mobileMenu = document.querySelector('.mobile-menu');

mobileMenuButton.addEventListener('click', () => {
    mobileMenu.classList.toggle('show');
});
