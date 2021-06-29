# *-* utf-8 *-*
import csv
from collections import namedtuple
import random
Calle = namedtuple("Calle","nombre,municipio")

result = []
with open("vialSevilla.csv", encoding = "latin1") as f:
    lector = csv.reader(f)
    next(lector)
    for registro in lector:
        if (registro[3]=="CALLE" or registro[3]=="AVENIDA") and not "SIN NOMBRE" in registro[4]:
            result.append([registro[5],registro[-1],registro[4]])

with open("vialSevillaFiltrado.csv", "w", newline="", encoding="latin1") as f:
    writer = csv.writer(f)
    writer.writerows(result)
        