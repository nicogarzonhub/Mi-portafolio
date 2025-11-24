#!/usr/bin/env python3
"""
usuarios.py - manejo simple de usuarios via CSV
"""
import csv
from getpass import getpass

USUARIOS_CSV = "usuarios.csv"
MAX_INTENTOS = 3

def _leer_usuarios():
    users = {}
    try:
        with open(USUARIOS_CSV, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for r in reader:
                users[r['usuario']] = r
    except FileNotFoundError:
        pass
    return users

def login():
    users = _leer_usuarios()
    for intento in range(1, MAX_INTENTOS+1):
        usuario = input("Usuario: ").strip()
        contrasena = getpass("Contraseña: ").strip()
        u = users.get(usuario)
        if u and u.get("contrasena") == contrasena and u.get("rol") == "ADMIN":
            print("Login exitoso.")
            return u
        else:
            print(f"Credenciales incorrectas. Intento {intento}/{MAX_INTENTOS}")
    return None

def login_required():
    u = login()
    return u is not None
