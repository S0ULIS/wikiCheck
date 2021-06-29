import csv
result = []
with open("matematicos.csv",encoding="Latin1") as f:
    lector = csv.reader(f)
    for linea in lector:
        result.append(linea)

with open('office.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(sorted(result,key=lambda x: x[2]))
