// URL del servidor JSON Server o API
const API_URL = "http://localhost:3000/products";

// Referencias del DOM
const form = document.getElementById("productForm");
const nameInput = document.getElementById("name");
const priceInput = document.getElementById("price");
const list = document.getElementById("productList");
const syncBtn = document.getElementById("syncBtn");

// Arreglo global que guarda los productos
let products = [];

/* Cargar datos guardados en LocalStorage cuando inicia la página */
document.addEventListener("DOMContentLoaded", () => {
    loadLocalProducts();
    renderProducts();
});

/* Evento para agregar productos */
form.addEventListener("submit", e => {
    e.preventDefault();
    addProduct();
});

/* Evento para sincronizar con API */
syncBtn.addEventListener("click", () => {
    fetchProducts();
});

/* Validar campos del formulario */
function validateFields(name, price) {
    if (!name || !price || price <= 0) {
        alert("Datos inválidos");
        return false;
    }
    return true;
}

/* Agregar producto */
function addProduct() {

    const name = nameInput.value.trim();
    const price = Number(priceInput.value);

    if (!validateFields(name, price)) return;

    const product = {
        id: Date.now(),
        name,
        price
    };

    products.push(product);

    saveLocalProducts();
    renderProducts();
    createProductAPI(product);

    form.reset();
}

/* Renderizar productos en el DOM */
function renderProducts() {

    list.innerHTML = "";

    products.forEach(product => {

        const li = document.createElement("li");
        li.textContent = `${product.name} - $${product.price}`;

        const deleteBtn = document.createElement("button");
        deleteBtn.textContent = "Eliminar";

        deleteBtn.addEventListener("click", () => {
            deleteProduct(product.id);
        });

        li.appendChild(deleteBtn);
        list.appendChild(li);
    });
}

/* Eliminar producto */
function deleteProduct(id) {

    products = products.filter(product => product.id !== id);

    saveLocalProducts();
    renderProducts();
    deleteProductAPI(id);
}

/* Guardar en LocalStorage */
function saveLocalProducts() {
    localStorage.setItem("products", JSON.stringify(products));
}

/* Cargar desde LocalStorage */
function loadLocalProducts() {
    const data = localStorage.getItem("products");
    if (data) {
        products = JSON.parse(data);
    }
}

/* Obtener productos desde API */
async function fetchProducts() {

    try {
        const response = await fetch(API_URL);
        const data = await response.json();

        console.log("Datos obtenidos de API:", data);

    } catch (error) {
        console.error("Error al obtener datos", error);
    }
}

/* Crear producto en API */
async function createProductAPI(product) {

    try {
        const response = await fetch(API_URL, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(product)
        });

        const data = await response.json();
        console.log("Producto enviado a API:", data);

    } catch (error) {
        console.error("Error al enviar producto", error);
    }
}

/* Eliminar producto en API */
async function deleteProductAPI(id) {

    try {
        await fetch(`${API_URL}/${id}`, {
            method: "DELETE"
        });

        console.log("Producto eliminado en API");

    } catch (error) {
        console.error("Error al eliminar en API", error);
    }
}

/* Actualizar producto en API */
async function updateProductAPI(product) {

    try {
        await fetch(`${API_URL}/${product.id}`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(product)
        });

        console.log("Producto actualizado en API");

    } catch (error) {
        console.error("Error al actualizar producto", error);
    }
}
