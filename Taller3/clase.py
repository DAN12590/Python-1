from csv import DictReader
from main import *

def mostrar_pkmn(pkm):
    print(f"Pokemon #{pkm["#"]}: {pkm["Name"]}")
    print(f"- Tipos: {pkm["Type 1"]} {pkm["Type 2"]}")
    print(f"- Generación {pkm["Generation"]}")
    if pkm["Legendary"] == "True":
        print("- Es legendario")

def buscar_por_nombre(csvreader):
    nombre = input("Nombre a buscar: ")
    for pkm in csvreader:  #Esto inicia un bucle for que recorre cada fila del archivo CSV. Cada vez que pasa por una fila,pkm es un diccionario que contiene los datos de un solo Pokémon
        if pkm["Name"].lower() == nombre.lower(): #Si pkm es el diccionario de Bulbasaur, entonces pkm["Name"] será "Bulbasaur"
            mostrar_pkmn(pkm)

with open("pokemon.txt") as pokemons:
    csvreader = DictReader(pokemons) #convierte cada fila en un diccionario,claves del diccionario son los nombres de las columnas del archivo

    while True:
        print("1. Buscar por nombre")
        print("2. Buscar por tipo")
        print("3. Legendarios por generación")
        print("4. Contar pokemon por generación elegida")
        print("5. Contar pokemon por generación")
        print("6. Salir")
        opcion = input("Elige una opción: ")
        match opcion:
            case "1":
                buscar_por_nombre(csvreader)
            case "2":
                buscar_por_tipo(csvreader)
            case "3":
                buscar_legendarios_por_generacion(csvreader)
            case "4":
                contar_pokemons_por_generacion_elegida(csvreader)
            case "5":
                contar_pokemons_por_generacion(csvreader)
            case "6":
                print("Hasta luego")
                break
            case _:
                print("Opción incorrecta")
        
        pokemons.seek(0)