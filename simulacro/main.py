#!/usr/bin/env python3
"""
main.py - Entrada principal de la aplicación de consola TechLab
"""
from usuarios import login_required, login
from equipos import menu_equipos
from prestamos import menu_prestamos
from reportes import menu_reportes

def main():
    print("Bienvenido a TechLab - Gestión de Inventario y Préstamos")
    if not login_required():
        print("Acceso denegado. Saliendo.")
        return
    while True:
        print("\nMenú principal:")
        print("1) Gestionar equipos")
        print("2) Gestionar préstamos")
        print("3) Reportes")
        print("4) Salir")
        choice = input("Seleccione una opción: ").strip()
        if choice == "1":
            menu_equipos()
        elif choice == "2":
            menu_prestamos()
        elif choice == "3":
            menu_reportes()
        elif choice == "4":
            print("Cerrando sesión. ¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

if __name__ == '__main__':
    main()
