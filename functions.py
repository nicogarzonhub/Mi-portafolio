# Print
def saludar():
    print("Hola a todos!")

saludar()

# Return
# def sumar(a, b):
#     return a + b

# resultado = sumar(3, 5)
# print(resultado)

# # var locals / globals
# x = 10  # global

# def prueba():
#     x = 5
#     print("Local:", x)

# prueba()
# print("Global:", x)

# # Example 1
# usuarios = []

# nombre = input("Nombre: ")
# edad = int(input("Edad: "))
# usuarios.append({"nombre": nombre, "edad": edad})
# print("Usuario creado!")

# # --------

# def pedir_datos_usuario():
#     nombre = input("Nombre: ")
#     edad = int(input("Edad: "))
#     return {"nombre": nombre, "edad": edad}

# def agregar_usuario(lista, usuario):
#     lista.append(usuario)
#     print("Usuario agregado!")

# usuarios = []
# nuevo = pedir_datos_usuario()
# agregar_usuario(usuarios, nuevo)

# # Example 2
# def validar_usuario(nombre, edad):
#     if nombre.strip() == "":
#         return False

#     if not isinstance(edad, int) or edad <= 0:
#         return False

#     return True

# print(validar_usuario("Ana", 20))  # True
# print(validar_usuario("", 20))     # False

# # Params
# def saludar(nombre="estudiante"):
#     print(f"Hola, {nombre}!")

# saludar()
# saludar("Brahian")
