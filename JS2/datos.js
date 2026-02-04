// ------------------------------
// Creación de productos (objeto)
// ------------------------------

// Lista de productos almacenados dentro de un objeto
const productos = {
    producto1: { id: 1, nombre: "Laptop", precio: 2500 },
    producto2: { id: 2, nombre: "Mouse", precio: 80 },
    producto3: { id: 3, nombre: "Teclado", precio: 150 }
};


// -----------------------------------
// Validación de los productos
// -----------------------------------

function validarProducto(producto) {

    // Se verifica que cada propiedad exista y sea válida
    if (
        typeof producto.id !== "number" ||
        typeof producto.nombre !== "string" ||
        typeof producto.precio !== "number"
    ) {
        console.error("Producto inválido detectado:", producto);
        return false;
    }

    return true;
}


// Validar todos los productos
Object.values(productos).forEach(producto => {
    validarProducto(producto);
});


// -----------------------------------
// Uso de SET
// -----------------------------------

// Set con números repetidos
const numeros = new Set([1, 2, 3, 3, 4, 5, 5, 6]);

console.log("Contenido inicial del Set:");
console.log(numeros);


// Agregar un número nuevo
numeros.add(7);
console.log("Después de agregar el número 7:", numeros);


// Verificar si existe un número
console.log("¿Existe el número 3?:", numeros.has(3));


// Eliminar un número
numeros.delete(2);
console.log("Después de eliminar el número 2:", numeros);


// Recorrer el Set con for...of
console.log("Recorrido del Set:");
for (const numero of numeros) {
    console.log(numero);
}


// -----------------------------------
// Creación de MAP
// -----------------------------------

// Relaciona categoría con nombre del producto
const categoriasProductos = new Map();

categoriasProductos.set("Tecnología", "Laptop");
categoriasProductos.set("Accesorios", "Mouse");
categoriasProductos.set("Periféricos", "Teclado");


// -----------------------------------
// Iteraciones solicitadas
// -----------------------------------

// Recorrer objeto con for...in
console.log("Listado de productos:");

for (const clave in productos) {
    console.log(clave, productos[clave]);
}


// Usar Object.keys()
console.log("Claves del objeto:");
console.log(Object.keys(productos));


// Usar Object.values()
console.log("Valores del objeto:");
console.log(Object.values(productos));


// Usar Object.entries()
console.log("Entradas del objeto:");
console.log(Object.entries(productos));


// Recorrer Set con for...of
console.log("Valores únicos del Set:");
for (const valor of numeros) {
    console.log(valor);
}


// Recorrer Map con forEach
console.log("Categorías y productos:");

categoriasProductos.forEach((producto, categoria) => {
    console.log(`Categoría: ${categoria} - Producto: ${producto}`);
});


// -----------------------------------
// Pruebas finales
// -----------------------------------

console.log("Lista completa de productos:", productos);
console.log("Lista de números únicos (Set):", numeros);
console.log("Mapa de categorías:", categoriasProductos);
