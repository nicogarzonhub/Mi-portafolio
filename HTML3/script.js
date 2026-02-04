// mensaje de bienvenida al cargar la página
window.onload = function(){
    alert("Bienvenido a mi portafolio");
};

// cambiar texto al presionar botón
const btnTexto = document.getElementById("btnCambiarTexto");

btnTexto.addEventListener("click", function(){
    document.getElementById("textoSobre").textContent =
    "Gracias por visitar mi portafolio. Estoy aprendiendo JavaScript.";
});

// mostrar u ocultar contenido
const btnToggle = document.getElementById("btnToggle");
const contenido = document.getElementById("contenidoExtra");

btnToggle.addEventListener("click", function(){

    if(contenido.style.display === "none"){
        contenido.style.display = "block";
    }else{
        contenido.style.display = "none";
    }

});
