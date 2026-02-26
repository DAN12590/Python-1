with open("quijote.txt", encoding="UTF8") as archivo:
    contador_palabras = {}
    for lineas in archivo:
        palabras = lineas.split()  # Divide la línea en palabras
        for palabra in palabras:
            palabra = palabra.lower()  # Convierte la palabra a minúsculas
            if palabra in contador_palabras:
                contador_palabras[palabra] += 1  # Incrementa el contador si ya existe
            else:
                contador_palabras[palabra] = 1  # Si no existe, la agrega al diccionario

# Muestra el resultado
with open("contador_palabras.txt", "w") as respuesta:
    for palabra, count in contador_palabras.items():
        respuesta.write(f"{palabra}: {count} \n")