inventario = []

def agregar_producto():
    nombre = input("Ingresa el nombre del producto: ")
    cantidad = int(input("Ingresa la cantidad del producto: "))
    precio = float(input("Ingresa el precio del producto: "))

    producto = {
        "nombre": nombre,
        "cantidad": cantidad,
        "precio": precio
    }

    inventario.append(producto)
    print("Producto agregado!\n")


def mostrar_inventario():
    if len(inventario) == 0:
        print("No hay productos registrados\n")
    else:
        print("\n== INVENTARIO ==")
        for p in inventario:
            print(p)
        print()


def calcular_estadisticas():
    if len(inventario) == 0:
        print("No hay productos para calcular estadísticas\n")
        return

    total_items = sum(p["cantidad"] for p in inventario)
    total_valor = sum(p["cantidad"] * p["precio"] for p in inventario)

    print("\n=== ESTADÍSTICAS ===")
    print("Total de artículos:", total_items)
    print("Valor total del inventario:", total_valor, "\n")


while True:
    print("= MENÚ PRINCIPAL =")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Calcular estadísticas")
    print("4. Salir")
    print("=======")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        mostrar_inventario()
    elif opcion == "3":
        calcular_estadisticas()
    elif opcion == "4":
        print("Saliendo...")
        break
    else:
        print("Opción inválida\n")
