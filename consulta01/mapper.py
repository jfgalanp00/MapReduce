#!/usr/bin/python3
import sys

#¿Cuantas veces se han enfrentado los All Black a cada una de las demas selecciones?

header = sys.stdin.readline()

for linea in sys.stdin:
    datos = linea.strip().split(",")
    adversario = datos[3]

    print(f"{adversario} \t1")