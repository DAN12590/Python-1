from csv import DictReader

def buscar_pais(nombre_buscado):
    with open("usuarios.csv", "r") as archivo:
        lector = DictReader(archivo)  # Crea un lector de CSV que devuelve diccionarios
        """DictReader(archivo, delimiter=";")"""
        # Recorremos cada fila (que será un diccionario)
        for fila in lector:
            if fila["Nombre"].lower() == nombre_buscado.lower():  # Compara el nombre
                return fila["Pais"]  # Si coincide, devuelve el país
        
        # Si no se encuentra el nombre
        return "Nombre no encontrado"

# Pedimos al usuario un nombre para buscar
nombre = input("Introduce el nombre del usuario: ")

# Llamamos a la función y mostramos el país
pais = buscar_pais(nombre)
print(f"El país de {nombre} es: {pais}")