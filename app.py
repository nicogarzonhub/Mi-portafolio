


import servicios

from typing import List, Dict

Product = Dict[str, object]

def solicitar_float(prompt: str) -> float:
    while True:
        val = input(prompt)
        try:
            f = float(val)
            if f < 0:
                print("The value cannot be negative. Please try again.")
                continue
            return f
        except ValueError:
            print("Invalid entry. Please enter a valid number.")

def solicitar_int(prompt: str) -> int:
    while True:
        val = input(prompt)
        try:
            i = int(float(val))
            if i < 0:
                print("The value cannot be negative. Please try again.")
                continue
            return i
        except ValueError:
            print("Invalid entry. Please enter a valid number.")


def main():
    inventario: List[Product] = []
    {"nombre": "1984","autor":"Orwell" ,"categoria":"Novel","precio": 50, "cantidad": 2},
    {"nombre": "Lolita","autor" :"Vladimir N" , "categoria":"Novel","precio": 30, "cantidad": 5},
    {"nombre": "La odisea",  "autor":"Homero" ,"categoria" :"Poem","precio": 15, "cantidad": 3},
    {"nombre": "Dracula","autor":"Bram S" , "categoria": "Horror","precio": 25, "cantidad": 5},
    {"nombre": "Hamlet","autor":"William S" , "categoria":"Teatro","precio": 100, "cantidad": 2},
    
inventario= [
    {"nombre": "1984","autor":"Orwell" ,"categoria":"Novel","precio": 50, "cantidad": 2},
    {"nombre": "Lolita","autor" :"Vladimir N" , "categoria":"Novel","precio": 30, "cantidad": 5},
    {"nombre": "La odisea",  "autor":"Homero" ,"categoria" :"Poem","precio": 15, "cantidad": 3},
    {"nombre": "Dracula","autor":"Bram S" , "categoria": "Horror","precio": 25, "cantidad": 5},
    {"nombre": "Hamlet","autor":"William S" , "categoria":"Teatro","precio": 100, "cantidad": 2},
]
inventario_ordenado = sorted(inventario, key=lambda p: p["precio"], reverse=True)

# Tomamos solo los 3 primeros (los más caros)
top3 = inventario_ordenado[:3]

# Mostramos el Top 3
print("=== TOP 3 PRODUCTOS DE MAYOR A MENOR ===")
for producto in top3:
    print(f"{producto['nombre']} - ${producto['precio']}")  
    
    
        
    

    while True:
        print("= MENU =")
        print("1. Add product")
        print("2. Show inventory")
        print("3. Search product")
        print("4. Update product")
        print("5. Remove product")
        print("6. Inventory statistics")
        print("7. Leave..")
        print("==")

        opcion = input("Choose a option (1-9): ").strip()
        if opcion not in [str(i) for i in range(1, 10)]:
            print("Invalid option. Choose a number from 1 to 9.\n")
            continue

        try:
            if opcion == "1":
                nombre = input("Name of product: ").strip()
                autor = input("Author name: ").strip()
                categoria = input("Category: ").strip()
                precio = solicitar_float("Cost: ")
                cantidad = solicitar_int("Amount:")
                servicios.agregar_producto(inventario, nombre,autor,categoria,precio,cantidad)
                print("Added product.\n")

            elif opcion == "2":
                servicios.mostrar_inventario(inventario)

            elif opcion == "3":
                nombre = input("Name to search: ")
                p = servicios.buscar_producto(inventario, nombre)
                if p:
                    print(f"Product found!: {p['nombre']} — Precio: ${p['precio']:.2f} — Cantidad: {p['cantidad']}\n")
                else:
                    print("Product not found.\n")

            elif opcion == "4":
                nombre = input("Product name to be updated: ")
                if servicios.buscar_producto(inventario, nombre) is None:
                    print("Product does not exist.\n")
                    continue
                respuesta = input("¿Change the cost? (S/N): ").strip().lower()
                nuevo_precio = None
                if respuesta == "s":
                    nuevo_precio = solicitar_float("New cost: ")
                respuesta = input("¿Change the amount? (S/N): ").strip().lower()
                nueva_cantidad = None
                if respuesta == "s":
                    nueva_cantidad = solicitar_int("New amount: ")
                updated = servicios.actualizar_producto(inventario, nombre, nuevo_precio, nueva_cantidad)
                if updated:
                    print("Update product.\n")
                else:
                    print("Update error (product not found).\n")

            elif opcion == "5":
                nombre = input("Nombre del producto a eliminar: ")
                eliminado = servicios.eliminar_producto(inventario, nombre)
                if eliminado:
                    print("Producto eliminado!\n")
                else:
                    print("Producto no encontrado.\n")

            elif opcion == "6":
                stats = servicios.calcular_estadisticas(inventario)
                print("\n- Statistics -")
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
                print("----\n")

            elif opcion=="7":
                def main():