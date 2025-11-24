"""
servicios.py
Funciones para manejar el inventario en memoria (lista de diccionarios).

Estructura de cada producto:
{"nombre": str, "precio": float, "cantidad": int}
"""

from typing import List, Dict, Optional

Producto = Dict[str, object]  # 'nombre', 'precio', 'cantidad'

def agregar_producto(inventario: List[Producto], nombre: str, precio: float, cantidad: int) -> None:
    """
    Agrega un producto al inventario en memoria.
    Si el nombre ya existe, suma la cantidad y actualiza el precio al nuevo.
    Parámetros:
        inventario: lista donde se almacenan los productos.
        nombre: nombre del producto.
        precio: precio (float, >= 0).
        cantidad: cantidad (int, >= 0).
    Retorno: None
    """
    nombre = nombre.strip()
    for p in inventario:
        if p["nombre"].lower() == nombre.lower():
            # Fusionar: sumar cantidad y actualizar precio al nuevo
            p["cantidad"] += cantidad
            p["precio"] = float(precio)
            return
    inventario.append({"nombre": nombre, "precio": float(precio), "cantidad": int(cantidad)})


def mostrar_inventario(inventario: List[Producto]) -> None:
    """
    Muestra el inventario en un formato legible por consola.
    Parámetros:
        inventario: lista de productos.
    Retorno: None
    """
    if not inventario:
        print("El inventario está vacío.\n")
        return

    print("\n= INVENTARIO =")
    for i, p in enumerate(inventario, start=1):
        print(f"{i}. {p['nombre']} — Precio: ${p['precio']:.2f} — Cantidad: {p['cantidad']}")
    print()


def buscar_producto(inventario: List[Producto], nombre: str) -> Optional[Producto]:
    """
    Busca un producto por nombre (insensible a mayúsculas).
    Parámetros:
        inventario: lista de productos.
        nombre: nombre a buscar.
    Retorno:
        El dict del producto si se encuentra, o None si no existe.
    """
    nombre = nombre.strip()
    for p in inventario:
        if p["nombre"].lower() == nombre.lower():
            return p
    return None


def actualizar_producto(inventario: List[Producto], nombre: str, nuevo_precio: Optional[float] = None, nueva_cantidad: Optional[int] = None) -> bool:
    """
    Actualiza precio y/o cantidad de un producto existente.
    Parámetros:
        inventario: lista de productos.
        nombre: nombre del producto a actualizar.
        nuevo_precio: nuevo precio (float) si se quiere cambiar.
        nueva_cantidad: nueva cantidad (int) si se quiere cambiar.
    Retorno:
        True si se actualizó, False si no existe el producto.
    """
    p = buscar_producto(inventario, nombre)
    if p is None:
        return False

    if nuevo_precio is not None:
        p["precio"] = float(nuevo_precio)
    if nueva_cantidad is not None:
        p["cantidad"] = int(nueva_cantidad)
    return True


def eliminar_producto(inventario: List[Producto], nombre: str) -> bool:
    """
    Elimina un producto del inventario por nombre.
    Parámetros:
        inventario: lista de productos.
        nombre: nombre del producto a eliminar.
    Retorno:
        True si se eliminó, False si no se encontró.
    """
    nombre = nombre.strip()
    for p in list(inventario):  # iterar sobre copia para eliminar seguro
        if p["nombre"].lower() == nombre.lower():
            inventario.remove(p)
            return True
    return False


def calcular_estadisticas(inventario: List[Producto]) -> Dict[str, object]:
    """
    Calcula estadísticas del inventario:
      - unidades_totales: suma de cantidades
      - valor_total: suma de precio * cantidad
      - producto_mas_caro: dict {'nombre', 'precio'}
      - producto_mayor_stock: dict {'nombre', 'cantidad'}
    Parámetros:
        inventario: lista de productos.
    Retorno:
        dict con métricas.
    Nota: usa una lambda para subtotal opcional.
    """
    if not inventario:
        return {
            "unidades_totales": 0,
            "valor_total": 0.0,
            "producto_mas_caro": None,
            "producto_mayor_stock": None
        }

    subtotal = (lambda p: p["precio"] * p["cantidad"])  # lambda opcional solicitada

    unidades_totales = sum(int(p["cantidad"]) for p in inventario)
    valor_total = sum(subtotal(p) for p in inventario)

    producto_mas_caro = max(inventario, key=lambda p: p["precio"])
    producto_mayor_stock = max(inventario, key=lambda p: p["cantidad"])

    return {
        "unidades_totales": unidades_totales,
        "valor_total": valor_total,
        "producto_mas_caro": {"nombre": producto_mas_caro["nombre"], "precio": producto_mas_caro["precio"]},
        "producto_mayor_stock": {"nombre": producto_mayor_stock["nombre"], "cantidad": producto_mayor_stock["cantidad"]}
    }
