"""
csv.reader(): Lee el archivo CSV y devuelve cada fila como
 una lista de valores (en lugar de un diccionario).

csv.DictReader(): Lee el archivo CSV y devuelve cada fila como un diccionario,
 donde las claves son los nombres de las columnas del archivo.
"""
from csv import DictReader

with open("ejemplo.csv", "r") as archivo:
    lector = DictReader(archivo)  # Crea un lector para el archivo CSV
    for fila in lector:  # Recorre cada fila del archivo
        print(fila)  # Imprime cada fila como una lista