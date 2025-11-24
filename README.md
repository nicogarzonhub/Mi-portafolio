# Mi-portafolio
# Lista donde se guardan los productos
inventario = []

# ---- Crear producto ----
def agregar_producto():
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio del producto: "))
    cantidad = int(input("Cantidad del producto: "))

    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    inventario.append(producto)
    print("Producto agregado correctamente.")

# ---- Listar productos ----
def listar_productos():
    if not inventario:
        print("No hay productos.")
        return

    for i, p in enumerate(inventario):
        print(f"{i}. {p['nombre']} - Precio: {p['precio']} - Cantidad: {p['cantidad']}")

# ---- Aplicar descuento ----
def aplicar_descuento():
    listar_productos()

    indice = int(input("Elige el número del producto: "))

    if indice < 0 or indice >= len(inventario):
        print("Producto no válido.")
        return

    porcentaje = float(input("Porcentaje de descuento: "))

    producto = inventario[indice]

    # Cálculo del descuento
    descuento = producto["precio"] * (porcentaje / 100)
    nuevo_precio = producto["precio"] - descuento

    producto["precio"] = nuevo_precio

    print(f"Descuento aplicado. Nuevo precio: {nuevo_precio}")

# ---- Menú ----
def menu():
    while True:
        print("\n1. Agregar producto")
        print("2. Listar productos")
        print("3. Aplicar descuento")
        print("4. Salir")

        opcion = input("Elige opción: ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            listar_productos()
        elif opcion == "3":
            aplicar_descuento()
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")


# Iniciar programa
menu()
