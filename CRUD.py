import csv
import os

class Crud:

    def crear_archivo(self, archivo):
        if not os.path.exists(archivo):
            with open(archivo, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["nombre", "precio", "cantidad"])

    def crear(self, archivo, nombre, precio, cantidad):
        with open(archivo, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([nombre, precio, cantidad])
        
    def listar(self, archivo):
        with open(archivo, "r") as f:
            reader = csv.reader(f)
            next(reader)
            return list(reader)



inventario = []

def cargar_desde_csv():
    inventario.clear()
    try:
        with open("datos.csv", newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                fila["cantidad"] = int(fila["cantidad"])
                fila["precio"] = float(fila["precio"])
                inventario.append(fila)
    except FileNotFoundError:
        print("⚠️ El archivo datos.csv no existe aún.")


def guardar_en_csv():
    with open("datos.csv", "w", newline="", encoding="utf-8") as archivo:
        columnas = ["nombre", "cantidad", "precio"]
        escritor = csv.DictWriter(archivo, fieldnames=columnas)
        escritor.writeheader()
        escritor.writerows(inventario)


   
   
    # ELIMINAR UN PRODUCTO POR NOMBRE
 
def eliminar(self, archivo, nombre):
        filas = []
        eliminado = False

        with open(archivo, "r") as f:
            reader = csv.reader(f)
            encabezado = next(reader)
            for row in reader:
                if row[0].lower() != nombre.lower():
                    filas.append(row)
                else:
                    eliminado = True

        with open(archivo, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(encabezado)
            writer.writerows(filas)

        return eliminado

    #  ACTUALIZAR UN PRODUCTO POR NOMBRE 
    
def actualizar(self, archivo, nombre, nuevo_precio, nueva_cantidad):
        filas = []
        actualizado = False

        with open(archivo, "r") as f:
            reader = csv.reader(f)
            encabezado = next(reader)

            for row in reader:
                if row[0].lower() == nombre.lower():
                    filas.append([row[0], nuevo_precio, nueva_cantidad])
                    actualizado = True
                else:
                    filas.append(row)

        with open(archivo, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(encabezado)
            writer.writerows(filas)

        return actualizado
    


        


        