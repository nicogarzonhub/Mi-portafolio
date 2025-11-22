# Lista
inventario = []

# Crear función para agregar producto
def agregar_producto():
    """
    Agrega un producto
    """
    nombre = input("Ingresa el nombre del producto: ")
    precio = float(input("Ingresa el precio del producto: "))
    cantidad = int(input("Ingresa la cantidad del producto: "))
   
    producto = {
        "nombre": nombre,
        "cantidad": cantidad,
        "precio": precio
    }
    
    inventario.append(producto)
    print("Producto agregado!\n")


# Mostrar inventario
def mostrar_producto():
    """
    Muestra los productos del inventario
    """
    if len(inventario) == 0:
        print("No hay productos registrados\n")
    else:
        print("\n= INVENTARIO =")
        for p in inventario:
            print(p)
        print()


# Estadísticas de un producto específico
def calcular_estadisticas():
    if len(inventario) == 0:
        print("No hay productos para calcular estadísticas\n")
        return

    nombre = input("Ingresa el nombre del producto que quieres calcular: ")

    for p in inventario:
        if p["nombre"].lower() == nombre.lower():
            total_items = p["cantidad"]
            total_valor = p["cantidad"] * p["precio"]

            print("\n📊 ESTADÍSTICAS DEL PRODUCTO 📊")
            print(f"Producto: {p['nombre']}")
            print(f"Cantidad total: {total_items}")
            print(f"Valor total: ${total_valor:,.2f}\n")
            return
    
    print("Ese producto no existe.\n")


# Eliminar productos
def eliminar_producto():
    if len(inventario) == 0:
        print("No hay productos que eliminar\n")
        return

    mostrar_producto()
    nombre = input("Producto que quieres eliminar: ")

    encontrado = False
    for p in inventario:
        if p["nombre"].lower() == nombre.lower():
            inventario.remove(p)
            print("Producto removido\n")
            encontrado = True
            break

    if not encontrado:
        print("Ese producto no existe\n")


#  ESTADÍSTICAS TOTALES — VERSIÓN CORREGIDA 
def estadisticas_totales():
    if not inventario:
        print("No hay productos en el inventario.\n")
        return

    # Lambda para subtotal
    subtotal = lambda p: p["precio"] * p["cantidad"]

    # Unidades totales
    unidades_totales = sum(p["cantidad"] for p in inventario)

    # Valor total del inventario
    valor_total = sum(subtotal(p) for p in inventario)

    # Producto más caro
    producto_mas_caro = max(inventario, key=lambda p: p["precio"])

    # Producto con mayor stock
    producto_mayor_stock = max(inventario, key=lambda p: p["cantidad"])

    print("\n ESTADÍSTICAS DEL INVENTARIO ")
    print(f" Unidades totales: {unidades_totales}")
    print(f" Valor total del inventario: ${valor_total:,.2f}")
    print(f" Producto más caro: {producto_mas_caro['nombre']} (${producto_mas_caro['precio']})")
    print(f" Producto con mayor stock: {producto_mayor_stock['nombre']} ({producto_mayor_stock['cantidad']} unidades)\n")

