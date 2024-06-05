#¿Cuantas veces ha ganado los All Black a cada seleccion?
#   En la columna result, i numero positivo significa Que los All Black han ganado, negativo es derrota

#!/usr/bin/python3
import sys

header = sys.stdin.readline()

for linea in sys.stdin:
    datos = linea.strip().split(",")
    adversario = datos[3]
    resultado = datos[2]

    if int(resultado) > 0:
        print(f"{adversario}\t1{resultado}")