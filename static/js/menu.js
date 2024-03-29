const barraLateral = document.querySelector(".barra-lateral");
const spans = document.querySelectorAll("span");
const palanca = document.querySelector(".switch");
const circulo = document.querySelector(".circulo");
const menu = document.querySelector(".menu");
const main = document.querySelector("main");

// Recuperar el estado del modo oscuro desde el almacenamiento local
const isDarkMode = localStorage.getItem("darkMode") === "true";

// Función para activar o desactivar el modo oscuro
const toggleDarkMode = () => {
    let body = document.body;
    body.classList.toggle("dark-mode");

    // Guardar el estado del modo oscuro en el almacenamiento local
    const currentMode = body.classList.contains("dark-mode") ? "true" : "false";
    localStorage.setItem("darkMode", currentMode);

    circulo.classList.toggle("prendido");
};

// Aplicar el modo oscuro si estaba activo antes
if (isDarkMode) {
    toggleDarkMode();
}

menu.addEventListener("click", () => {
    barraLateral.classList.toggle("max-barra-lateral");
    if (barraLateral.classList.contains("max-barra-lateral")) {
        menu.children[0].style.display = "none";
        menu.children[1].style.display = "block";
    } else {
        menu.children[0].style.display = "block";
        menu.children[1].style.display = "none";
    }
});

palanca.addEventListener("click", toggleDarkMode);

let listElements = document.querySelectorAll('.nav__button--click');

listElements.forEach(listElement =>{
    listElement.addEventListener('click', ()=>{
        listElement.classList.toggle('arrow');

        let height = 0;
        let menu = listElement.nextElementSibling;
        if(menu.clientHeight == 0){
            height = menu.scrollHeight;
        }
        menu.style.height = `${height}px`;
    })
});