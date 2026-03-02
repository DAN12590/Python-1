with open("ejemploRead", "r") as archivo:
    contenido = archivo.read()  # Lee todo el archivo de una vez y lo guarda en "contenido"
    print(contenido)  # Muestra todo el contenido

    #lee todo el contenido del archivo en una sola vez. 
    #Devuelve una cadena de texto con todo el contenido, incluidos los saltos de línea

with open("ejemploRead", "r") as archivo:
    print(archivo.read(10))  # Lee los primeros 10 caracteres
    archivo.seek(0)  # Mueve el cursor al principio del archivo
    print(archivo.read())  # Lee todo el archivo desde el principio