import csv

# Crear el archivo CSV con algunos estudiantes
def crear_archivo_csv():
    with open('estudiantes.csv', 'w', newline='') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(['Nombre', 'Edad', 'Grado'])  # Encabezados
        escritor.writerow(['Juan', 16, '10'])  # Estudiante 1
        escritor.writerow(['Ana', 15, '9'])   # Estudiante 2
        escritor.writerow(['Luis', 17, '11'])  # Estudiante 3

# Completa esta función para agregar un nuevo estudiante al archivo
def agregar_estudiante(nombre, edad, grado):
    with open('estudiantes.csv', 'a', newline='') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([nombre, edad, grado])  # Agregar estudiante

# Completa esta función para leer y mostrar todos los estudiantes
def mostrar_estudiantes():
    with open('estudiantes.csv', 'r') as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            print(f"Nombre: {fila[0]}, Edad: {fila[1]}, Grado: {fila[2]}")

# Ejemplo de uso
crear_archivo_csv()  # Crear el archivo CSV inicial
agregar_estudiante('Pedro', 16, '10')  # Aquí el estudiante que agregues
mostrar_estudiantes()  # Mostrar todos los estudiantes