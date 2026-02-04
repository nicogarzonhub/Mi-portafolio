
// Selección de elementos del DOM

const inputNota = document.getElementById("inputNota");
const btnAgregar = document.querySelector("#btnAgregar");
const listaNotas = document.getElementById("listaNotas");

// Verificar que los elementos existen
console.log(inputNota);
console.log(btnAgregar);
console.log(listaNotas);



// Arreglo donde se guardan notas

let notas = [];


// Cargar notas desde Local Storage


const notasGuardadas = localStorage.getItem("notas");

if (notasGuardadas) {

    notas = JSON.parse(notasGuardadas);
    console.log(`Se cargaron ${notas.length} notas`);

    notas.forEach(nota => crearNotaDOM(nota));
}


// Función para crear notas en el DOM


function crearNotaDOM(textoNota) {

    const li = document.createElement("li");
    li.textContent = textoNota;

    // Botón eliminar
    const btnEliminar = document.createElement("button");
    btnEliminar.textContent = "Eliminar";

    // Evento eliminar nota
    btnEliminar.addEventListener("click", function() {

        listaNotas.removeChild(li);

        // eliminar del arreglo
        notas = notas.filter(nota => nota !== textoNota);

        // actualizar local storage
        localStorage.setItem("notas", JSON.stringify(notas));

        console.log("Nota eliminada:", textoNota);
    });

    li.appendChild(btnEliminar);
    listaNotas.appendChild(li);
}


// Evento para agregar notas


btnAgregar.addEventListener("click", function() {

    const texto = inputNota.value.trim();

    // Validar que no esté vacío
    if (texto === "") {
        alert("Debes escribir una nota");
        return;
    }

    // Guardar en arreglo
    notas.push(texto);

    // Guardar en local storage
    localStorage.setItem("notas", JSON.stringify(notas));

    // Crear nota en DOM
    crearNotaDOM(texto);

    console.log("Nota agregada:", texto);

    // Limpiar input y enfocar
    inputNota.value = "";
    inputNota.focus();
});
