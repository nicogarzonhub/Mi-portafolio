import servicios
from CRUD import Crud

crud = Crud()
archivo = "datos.csv"

crud.crear_archivo(archivo)



# Menú principal
while True:
    print("= MENÚ PRINCIPAL =")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Calcular producto")
    print("4. Eliminar producto")
    print("5. Estadisticas inventario")
    print("6. Salir")
    print("====")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        servicios.agregar_producto()
    elif opcion == "2":
        servicios.mostrar_producto()
    elif opcion == "3":
        servicios.calcular_estadisticas()

    elif opcion == "4":
        servicios.eliminar_producto()
    elif opcion == "5":
        servicios.estadisticas_totales()
    elif opcion == "6":
        print("Saliendo..")

        
        break

    

    
    else:
        print("Opción inválida\n")

        

