"""
app.py
Menú principal que integra servicios y archivos.
Opciones:
1-Agregar
2-Mostrar
3-Buscar
4-Actualizar
5-Eliminar
6-Estadísticas
7-Guardar CSV
8-Cargar CSV
9-Salir
"""

import servicios
import archivos
from typing import List, Dict

Producto = Dict[str, object]

def solicitar_float(prompt: str) -> float:
    while True:
        val = input(prompt)
        try:
            f = float(val)
            if f < 0:
                print("El valor no puede ser negativo. Intenta de nuevo.")
                continue
            return f
        except ValueError:
            print("Entrada inválida. Ingresa un número válido.")

def solicitar_int(prompt: str) -> int:
    while True:
        val = input(prompt)
        try:
            i = int(float(val))
            if i < 0:
                print("La cantidad no puede ser negativa. Intenta de nuevo.")
                continue
            return i
        except ValueError:
            print("Entrada inválida. Ingresa un entero válido.")

def mostrar_resumen_carga(cargados: int, invalidas: int, accion: str) -> None:
    print("\n--- Resumen de carga ---")
    print(f"Productos válidos cargados: {cargados}")
    print(f"Filas inválidas omitidas: {invalidas}")
    print(f"Acción realizada: {accion}")
    print("------------------------\n")

def main():
    inventario: List[Producto] = []

    while True:
        print("= MENÚ PRINCIPAL =")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Buscar producto")
        print("4. Actualizar producto")
        print("5. Eliminar producto")
        print("6. Estadísticas del inventario")
        print("7. Guardar CSV")
        print("8. Cargar CSV")
        print("9. Salir")
        print("===================")

        opcion = input("Elige una opción (1-9): ").strip()
        if opcion not in [str(i) for i in range(1, 10)]:
            print("Opción inválida. Elige un número del 1 al 9.\n")
            continue

        try:
            if opcion == "1":
                nombre = input("Nombre: ").strip()
                precio = solicitar_float("Precio: ")
                cantidad = solicitar_int("Cantidad: ")
                servicios.agregar_producto(inventario, nombre, precio, cantidad)
                print("Producto agregado.\n")

            elif opcion == "2":
                servicios.mostrar_inventario(inventario)

            elif opcion == "3":
                nombre = input("Nombre a buscar: ")
                p = servicios.buscar_producto(inventario, nombre)
                if p:
                    print(f"Encontrado: {p['nombre']} — Precio: ${p['precio']:.2f} — Cantidad: {p['cantidad']}\n")
                else:
                    print("Producto no encontrado.\n")

            elif opcion == "4":
                nombre = input("Nombre del producto a actualizar: ")
                if servicios.buscar_producto(inventario, nombre) is None:
                    print("Producto no existe.\n")
                    continue
                respuesta = input("¿Cambiar precio? (S/N): ").strip().lower()
                nuevo_precio = None
                if respuesta == "s":
                    nuevo_precio = solicitar_float("Nuevo precio: ")
                respuesta = input("¿Cambiar cantidad? (S/N): ").strip().lower()
                nueva_cantidad = None
                if respuesta == "s":
                    nueva_cantidad = solicitar_int("Nueva cantidad: ")
                updated = servicios.actualizar_producto(inventario, nombre, nuevo_precio, nueva_cantidad)
                if updated:
                    print("Producto actualizado.\n")
                else:
                    print("No se pudo actualizar (producto no encontrado).\n")

            elif opcion == "5":
                nombre = input("Nombre del producto a eliminar: ")
                eliminado = servicios.eliminar_producto(inventario, nombre)
                if eliminado:
                    print("Producto eliminado!\n")
                else:
                    print("Producto no encontrado.\n")

            elif opcion == "6":
                stats = servicios.calcular_estadisticas(inventario)
                print("\n--- ESTADÍSTICAS ---")
                print(f"Unidades totales: {stats['unidades_totales']}")
                print(f"Valor total inventario: ${stats['valor_total']:,.2f}")
                pmc = stats["producto_mas_caro"]
                pms = stats["producto_mayor_stock"]
                if pmc:
                    print(f"Producto más caro: {pmc['nombre']} (${pmc['precio']:.2f})")
                else:
                    print("Producto más caro: N/A")
                if pms:
                    print(f"Producto con mayor stock: {pms['nombre']} ({pms['cantidad']} unidades)")
                else:
                    print("Producto con mayor stock: N/A")
                print("--------------------\n")

            elif opcion == "7":
                ruta = input("Ruta archivo destino (por ejemplo datos.csv): ").strip()
                archivos.guardar_csv(inventario, ruta)

            elif opcion == "8":
                ruta = input("Ruta archivo a cargar (por ejemplo datos.csv): ").strip()
                productos_cargados, filas_invalidas = archivos.cargar_csv(ruta)
                if not productos_cargados and filas_invalidas == 0:
                    # pudo ser archivo inexistente o encabezado inválido, ya informado por cargar_csv
                    continue

                # Mostrar política de fusión al usuario
                print("\nPolítica de fusión por defecto: si el nombre existe, se SUMA la cantidad y se ACTUALIZA el precio al nuevo.")
                eleccion = input("¿Sobrescribir inventario actual? (S/N): ").strip().lower()
                if eleccion == "s":
                    inventario.clear()
                    inventario.extend(productos_cargados)
                    accion = "Reemplazado"
                else:
                    # fusionar
                    for p in productos_cargados:
                        servicios.agregar_producto(inventario, p["nombre"], p["precio"], p["cantidad"])
                    accion = "Fusionado"

                mostrar_resumen_carga(len(productos_cargados), filas_invalidas, accion)

            elif opcion == "9":
                print("Saliendo... Hasta luego.")
                break

        except Exception as e:
            # Capturar errores inesperados y volver al menú.
            print(f"Ha ocurrido un error: {e}\n")


if __name__ == "__main__":
    main()
