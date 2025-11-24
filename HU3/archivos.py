"""
archivos.py
Funciones para persistencia: guardar y cargar CSV con validaciones y manejo de errores.
CSV: encabezado obligatorio: nombre,precio,cantidad
"""

import csv
from typing import List, Dict, Tuple

Producto = Dict[str, object]

def guardar_csv(inventario: List[Producto], ruta: str, incluir_header: bool = True) -> None:
    """
    Guarda el inventario en ruta (CSV). Maneja errores sin cerrar la app.
    Parámetros:
        inventario: lista de productos.
        ruta: ruta/archivo destino.
        incluir_header: si True escribe el encabezado.
    Retorno: None
    """
    if not inventario:
        print("No hay datos para guardar. Inventario vacío.\n")
        return

    try:
        with open(ruta, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f, delimiter=',')
            if incluir_header:
                writer.writerow(["nombre", "precio", "cantidad"])
            for p in inventario:
                writer.writerow([p["nombre"], p["precio"], p["cantidad"]])
        print(f"Inventario guardado en: {ruta}\n")
    except PermissionError:
        print("Error: permiso denegado al intentar escribir el archivo. Verifica permisos.\n")
    except OSError as e:
        print(f"Error al escribir el archivo: {e}\n")


def _validar_encabezado(header: List[str]) -> bool:
    expected = ["nombre", "precio", "cantidad"]
    return [h.strip().lower() for h in header] == expected


def cargar_csv(ruta: str) -> Tuple[List[Producto], int]:
    """
    Carga un CSV desde 'ruta' y retorna (lista_productos, filas_invalidas).
    Validaciones:
      - encabezado exacto: nombre,precio,cantidad
      - cada fila tiene 3 columnas
      - precio -> float (>=0), cantidad -> int (>=0)
    Si hay filas inválidas se omiten y se cuenta.
    Excepciones manejadas con mensajes claros.
    Parámetros:
        ruta: ruta al archivo CSV.
    Retorno:
        (lista_valida_de_productos, contador_filas_invalidas)
    """
    productos = []
    filas_invalidas = 0

    try:
        with open(ruta, newline="", encoding="utf-8") as f:
            reader = csv.reader(f, delimiter=',')
            try:
                header = next(reader)
            except StopIteration:
                print("El archivo está vacío.\n")
                return [], 0

            if not _validar_encabezado(header):
                print("Encabezado inválido. Se espera: nombre,precio,cantidad\n")
                return [], 0

            for i, row in enumerate(reader, start=2):
                # Validar longitud de columnas
                if len(row) != 3:
                    filas_invalidas += 1
                    continue
                nombre, precio_str, cantidad_str = row
                try:
                    precio = float(precio_str)
                    cantidad = int(float(cantidad_str))  # admitir "1.0" como int
                    if precio < 0 or cantidad < 0:
                        raise ValueError("Valores negativos no permitidos")
                except (ValueError, TypeError):
                    filas_invalidas += 1
                    continue

                productos.append({"nombre": nombre.strip(), "precio": float(precio), "cantidad": int(cantidad)})
    except FileNotFoundError:
        print(f"Archivo no encontrado: {ruta}\n")
        return [], 0
    except UnicodeDecodeError:
        print("Error de codificación al leer el archivo. Verifica la codificación (debe ser UTF-8).\n")
        return [], 0
    except Exception as e:
        print(f"Error al leer el archivo: {e}\n")
        return [], 0

    return productos, filas_invalidas
