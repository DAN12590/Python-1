from csv import DictReader

with open("notas.csv") as archivo: #Abre el archivo
    lectorcsv = DictReader(archivo, delimiter=";") #delimiter=";" le dice que los datos están separados por ;
    #lectorcsv es como una lista de diccionarios

    susp_tarea1 = 0
    for linea in lectorcsv:
        if int(linea["Tarea 1"]) < 5:
            susp_tarea1 += 1
    print("Suspensos tarea 1:", susp_tarea1)