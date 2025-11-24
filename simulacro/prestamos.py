#!/usr/bin/env python3
"""
prestamos.py - solicitar, aprobar/rechazar, registrar devoluciones
"""
import csv
from datetime import datetime, date
from equipos import _leer_equipos, _escribir_equipos

PRESTAMOS_CSV = "prestamos.csv"
FIELDNAMES = ['prestamo_id','equipo_id','nombre_equipo','usuario_prestatario','tipo_usuario','fecha_solicitud','fecha_entrega_estado','dias','retraso','estado','mes','anio']

LIMITES = {'Estudiante':3,'Instructor':7,'Administrativo':10}

def _leer_prestamos():
    prestamos = []
    try:
        with open(PRESTAMOS_CSV, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for r in reader:
                prestamos.append(r)
    except FileNotFoundError:
        pass
    return prestamos

def _escribir_prestamos(prestamos):
    with open(PRESTAMOS_CSV, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(prestamos)

def generar_id(prestamos):
    ids = [int(p['prestamo_id']) for p in prestamos] if prestamos else []
    return str(max(ids)+1) if ids else "1"

def solicitar_prestamo():
    equipos = _leer_equipos()
    disponibles = [e for e in equipos if e['estado_actual']=="DISPONIBLE"]
    if not disponibles:
        print("No hay equipos disponibles.")
        return
    print("Equipos disponibles:")
    for e in disponibles:
        print(f"{e['equipo_id']}) {e['nombre_equipo']}")
    eid = input("ID del equipo a solicitar: ").strip()
    equipo = next((x for x in equipos if x['equipo_id']==eid and x['estado_actual']=="DISPONIBLE"), None)
    if not equipo:
        print("Equipo no disponible.")
        return
    usuario = input("Nombre del solicitante: ").strip()
    tipo = input("Tipo de usuario (Estudiante/Instructor/Administrativo): ").strip()
    prestamos = _leer_prestamos()
    pid = generar_id(prestamos)
    hoy = datetime.now().date().isoformat()
    prest = {
        'prestamo_id':pid,
        'equipo_id':equipo['equipo_id'],
        'nombre_equipo':equipo['nombre_equipo'],
        'usuario_prestatario':usuario,
        'tipo_usuario':tipo,
        'fecha_solicitud':hoy,
        'fecha_entrega_estado':'',
        'dias':'',
        'retraso':'',
        'estado':'PENDIENTE',
        'mes':str(datetime.now().month),
        'anio':str(datetime.now().year)
    }
    prestamos.append(prest)
    _escribir_prestamos(prestamos)
    print(f"Solicitud registrada con ID {pid} (PENDIENTE)")

def listar_prestamos(filtro=None):
    prestamos = _leer_prestamos()
    if filtro:
        prestamos = [p for p in prestamos if filtro(p)]
    if not prestamos:
        print("No hay préstamos.")
        return
    for p in prestamos:
        print(f"{p['prestamo_id']}) {p['nombre_equipo']} - {p['usuario_prestatario']} - {p['estado']}")

def aprobar_rechazar():
    prestamos = _leer_prestamos()
    pid = input("ID de préstamo a procesar: ").strip()
    p = next((x for x in prestamos if x['prestamo_id']==pid and x['estado']=='PENDIENTE'), None)
    if not p:
        print("No se encontró préstamo pendiente con ese ID.")
        return
    decision = input("Aprobar (A) / Rechazar (R): ").strip().upper()
    if decision == 'A':
        # Marcar equipo no disponible
        equipos = _leer_equipos()
        equipo = next((e for e in equipos if e['equipo_id']==p['equipo_id']), None)
        if equipo:
            equipo['estado_actual'] = "PRESTADO"
            _escribir_equipos(equipos)
        p['estado'] = 'APROBADO'
        # calcular fecha esperada (según límites) -- se guarda solo el estado actual
        print("Préstamo aprobado.")
    elif decision == 'R':
        p['estado'] = 'RECHAZADO'
        print("Préstamo rechazado.")
    else:
        print("Opción inválida.")
        return
    _escribir_prestamos(prestamos)

def registrar_devolucion():
    prestamos = _leer_prestamos()
    pid = input("ID del préstamo a devolver: ").strip()
    p = next((x for x in prestamos if x['prestamo_id']==pid and x['estado']=='APROBADO'), None)
    if not p:
        print("No hay préstamo aprobado con ese ID.")
        return
    fecha_entrega = datetime.now().date()
    fecha_solicitud = datetime.fromisoformat(p['fecha_solicitud']).date()
    dias_usados = (fecha_entrega - fecha_solicitud).days
    limite = LIMITES.get(p['tipo_usuario'], 0)
    retraso = max(0, dias_usados - limite)
    p['fecha_entrega_estado'] = fecha_entrega.isoformat()
    p['dias'] = str(dias_usados)
    p['retraso'] = str(retraso)
    p['estado'] = 'DEVUELTO'
    # marcar equipo disponible
    equipos = _leer_equipos()
    equipo = next((e for e in equipos if e['equipo_id']==p['equipo_id']), None)
    if equipo:
        equipo['estado_actual'] = "DISPONIBLE"
        _escribir_equipos(equipos)
    _escribir_prestamos(prestamos)
    print(f"Devolución registrada. Días usados: {dias_usados}, Retraso: {retraso}")

def historial():
    clave = input("Consultar por (1) usuario o (2) equipo ID: ").strip()
    prestamos = _leer_prestamos()
    if clave == '1':
        u = input("Nombre usuario: ").strip()
        fs = [p for p in prestamos if p['usuario_prestatario'].lower()==u.lower()]
    else:
        eid = input("ID equipo: ").strip()
        fs = [p for p in prestamos if p['equipo_id']==eid]
    if not fs:
        print("No se encontraron registros.")
        return
    for p in fs:
        print(p)

def menu_prestamos():
    while True:
        print("\n--- Gestión de Préstamos ---")
        print("1) Solicitar préstamo")
        print("2) Listar préstamos")
        print("3) Aprobar/Rechazar préstamo")
        print("4) Registrar devolución")
        print("5) Historial (usuario/equipo)")
        print("6) Volver")
        c = input("Opción: ").strip()
        if c=='1':
            solicitar_prestamo()
        elif c=='2':
            listar_prestamos()
        elif c=='3':
            aprobar_rechazar()
        elif c=='4':
            registrar_devolucion()
        elif c=='5':
            historial()
        elif c=='6':
            break
        else:
            print("Opción inválida.")
