#!/usr/bin/env python3
"""
reportes.py - exportar reportes mensuales/anuales (CSV)
"""
import csv
from prestamos import _leer_prestamos
from datetime import datetime

def exportar_mes_anio(mes, anio, destino):
    prestamos = _leer_prestamos()
    seleccion = [p for p in prestamos if p.get('mes')==str(mes) and p.get('anio')==str(anio)]
    if not seleccion:
        print("No hay registros para ese mes/año.")
        return
    keys = seleccion[0].keys()
    with open(destino, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(seleccion)
    print(f"Reporte exportado a {destino}")

def menu_reportes():
    while True:
        print("\n--- Reportes ---")
        print("1) Exportar reporte mensual")
        print("2) Exportar reporte anual")
        print("3) Volver")
        c = input("Opción: ").strip()
        if c=='1':
            mes = input("Mes (1-12): ").strip()
            anio = input("Año (ej. 2025): ").strip()
            destino = f"reporte_{mes}_{anio}.csv"
            exportar_mes_anio(mes, anio, destino)
        elif c=='2':
            anio = input("Año (ej. 2025): ").strip()
            destino = f"reporte_{anio}.csv"
            # agrupar todo el año
            prestamos = _leer_prestamos()
            seleccion = [p for p in prestamos if p.get('anio')==str(anio)]
            if not seleccion:
                print("No hay registros para ese año.")
            else:
                keys = seleccion[0].keys()
                with open(destino, 'w', newline='', encoding='utf-8') as f:
                    writer = csv.DictWriter(f, fieldnames=keys)
                    writer.writeheader()
                    writer.writerows(seleccion)
                print(f"Reporte anual exportado a {destino}")
        elif c=='3':
            break
        else:
            print("Opción inválida.")
