with open ("quijote.txt", "r") as archivo:
    contenido = archivo.readlines(200) #el 200 es el numero de caracteres que lee
    print(contenido)

with open("ejemploRead", "r") as archivo:
    lineas = archivo.readlines()  # Lee todas las líneas y las guarda en una lista
    print(lineas)  # Muestra la lista de líneas