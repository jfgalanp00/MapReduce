#!/usr/bin/python3

import sys

equipo_actual = None
resultado = None
contador = None

for linea in sys.stdin:
    equipo, valor = linea.strip().split("\t", 1)

    if valor :
        valor = int(valor)
    else:
        # Si el valor esta vcaio, ignora la linea
        continue

    if equipo_actual == equipo:
        contador += valor
    else:
        # evitamos problemas en la primera pasada
        if equipo_actual:
            print(f"{equipo_actual} {contador}")
        equipo_actual = equipo
        contador = valor

# evitamos problemas en la ultima pasada
if equipo_actual == equipo:
    print(f"{equipo_actual} {contador}")