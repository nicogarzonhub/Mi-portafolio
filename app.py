from CRUD import Crud


crud = Crud()
archivo = "datos.csv"

crud.crear_archivo(archivo)

# Lista
inventario = []

# Crear función para agregar producto
def agregar_producto():
    
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
    if len(inventario) == 0:
        print("No hay productos registrados\n")
    else:
        print("\n= INVENTARIO =")
        for p in inventario:
            print(p)
        print()

# Calcular estadísticas
def calcular_estadisticas():
    if len(inventario) == 0:
        print("No hay productos para calcular estadísticas\n")
        return

    nombre = input("Ingresa el nombre del producto que quieres calcular: ")

    for p in inventario:
        if p["nombre"].lower() == nombre.lower():
            total_items = p["cantidad"]
            total_valor = p["cantidad"] * p["precio"]

            print("\n ESTADÍSTICAS DEL PRODUCTO ")
            print("Producto:", p["nombre"])
            print("Cantidad total:", total_items)
            print("Valor total:", total_valor, "\n")
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

# Menú principal
while True:
    print("= MENÚ PRINCIPAL =")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Calcular estadísticas")
    print("4. Eliminar producto")
    print("5. Salir")
    print("=======")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        mostrar_producto()
    elif opcion == "3":
        calcular_estadisticas()
    elif opcion == "4":
        eliminar_producto()
    elif opcion == "5":
        print("Saliendo...")
        break
    else:
        print("Opción inválida\n")

        

