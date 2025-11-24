#!/usr/bin/env python3
"""
equipos.py - registrar, listar y consultar equipos (CSV)
"""
import csv
from datetime import datetime

EQUIPOS_CSV = "equipos.csv"
FIELDNAMES = ['equipo_id','nombre_equipo','categoria','estado_actual','fecha_registro']

def _leer_equipos():
    equipos = []
    try:
        with open(EQUIPOS_CSV, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for r in reader:
                equipos.append(r)
    except FileNotFoundError:
        pass
    return equipos

def _escribir_equipos(equipos):
    with open(EQUIPOS_CSV, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(equipos)

def generar_id(equipos):
    ids = [int(e['equipo_id']) for e in equipos] if equipos else []
    return str(max(ids)+1) if ids else "1"

def registrar_equipo():
    equipos = _leer_equipos()
    eid = generar_id(equipos)
    nombre = input("Nombre del equipo: ").strip()
    categoria = input("Categoría: ").strip()
    estado = "DISPONIBLE"
    fecha = datetime.now().isoformat()
    equipo = {'equipo_id':eid,'nombre_equipo':nombre,'categoria':categoria,'estado_actual':estado,'fecha_registro':fecha}
    equipos.append(equipo)
    _escribir_equipos(equipos)
    print(f"Equipo registrado con ID {eid}")

def listar_equipos():
    equipos = _leer_equipos()
    if not equipos:
        print("No hay equipos registrados.")
        return
    print("\nEquipos:")
    for e in equipos:
        print(f"{e['equipo_id']}) {e['nombre_equipo']} - {e['categoria']} - {e['estado_actual']}")

def consultar_equipo():
    equipos = _leer_equipos()
    q = input("ID o nombre para buscar: ").strip()
    found = [e for e in equipos if e['equipo_id']==q or e['nombre_equipo'].lower()==q.lower()]
    if not found:
        print("No se encontró.")
        return
    for e in found:
        print(e)

def menu_equipos():
    while True:
        print("\n--- Gestión de Equipos ---")
        print("1) Registrar equipo")
        print("2) Listar equipos")
        print("3) Consultar equipo")
        print("4) Volver")
        c = input("Opción: ").strip()
        if c=="1":
            registrar_equipo()
        elif c=="2":
            listar_equipos()
        elif c=="3":
            consultar_equipo()
        elif c=="4":
            break
        else:
            print("Opción inválida.")
