
# Solicitar nombre del producto

nombre = input("Ingrese el nombre del producto: ")

# Solicitar precio

precio = input("Ingrese el precio del producto: ")

while not precio.replace(".", "", 1).isdigit():
    print(" Error: el precio debe ser un número.")
    precio = input("Ingrese el precio del producto: ")

precio = float(precio)


# Solicitar cantidad

cantidad = input("Ingrese la cantidad del producto: ")

while not cantidad.isdigit():
    print(" Error: la cantidad debe ser un número entero.")
    cantidad = input("Ingrese la cantidad del producto: ")

cantidad = int(cantidad)


# Cálculo del costo total

costo_total = precio * cantidad


# Mostrar resultados

print(f"Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad} | Total: {costo_total}")


# Comentario final del programa
# Este programa solicita nombre, precio y cantidad,
# valida que el precio sea número decimal y la cantidad sea entero,
# calcula el costo total y muestra los datos en consola.