from csv import DictReader

with open("notas.csv") as archivo:
    lectorcsv = DictReader(archivo, delimiter=";")

    susp_tarea1 = 0
    for linea in lectorcsv:
        if int(linea["Tarea 1"]) < 5:
            susp_tarea1 += 1
    print("Suspensos tarea 1:", susp_tarea1)