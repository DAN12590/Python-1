with open("ejemploRead", "r") as archivo:
    linea = archivo.readline()  # Lee la primera línea
    print(linea)  # Imprime la primera línea
    linea = archivo.readline()  # Lee la segunda línea
    print(linea)  # Imprime la segunda línea