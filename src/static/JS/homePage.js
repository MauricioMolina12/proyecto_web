document.getElementById("sigup").addEventListener("click", function() {
    window.location.href = "/register";
});

document.getElementById("signin").addEventListener("click", function() {
    window.location.href = "/login";
});

document.getElementById("ruta").addEventListener("click", function(){
    window.location.href = "/map"
});


const mobileMenuButton = document.getElementById('mobile-menu');
const mobileMenu = document.querySelector('.mobile-menu');

mobileMenuButton.addEventListener('click', () => {
    mobileMenu.classList.toggle('show');
});
