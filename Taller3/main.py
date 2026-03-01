def mostrar_pkmn(pkm):
    print(f"Pokemon #{pkm['#']}: {pkm['Name']}")
    print(f"- Tipos: {pkm['Type 1']} {pkm['Type 2']}")
    print(f"- Generación {pkm['Generation']}")
    if pkm["Legendary"] == "True":
        print("- Es legendario")

def buscar_por_nombre(csvreader):
    nombre = input("Nombre a buscar: ")
    for pkm in csvreader:
        if pkm["Name"].lower() == nombre.lower():
            mostrar_pkmn(pkm)

def buscar_por_tipo(csvreader):
    suma_total = 0
    tipo = input("Tipo a buscar: ").lower()
    for pkm in csvreader:
        if tipo == pkm["Type 1"].lower() or tipo == pkm["Type 2"].lower():
            mostrar_pkmn(pkm)
            suma_total += 1
    print(f"La suma total es de {suma_total} pokemons")

def buscar_legendarios_por_generacion(csvreader):
    suma_total = 0
    generacion = input("Generación a buscar: ")
    for pkm in csvreader:
        if pkm["Legendary"] == "True" and pkm["Generation"] == generacion:
            mostrar_pkmn(pkm)
            suma_total += 1
    print(f"La suma total es de {suma_total} pokemons")

def contar_pokemons_por_generacion_elegida(csvreader):
    suma_total = 0
    generacion = input("Generación a buscar: ")
    for pkm in csvreader:
        if pkm["Generation"] == generacion:
            suma_total += 1
            mostrar_pkmn(pkm)
    print(f"La suma total es de {suma_total} pokemons")

def contar_pokemons_por_generacion(csvreader):
    cuenta = {}
    for pkm in csvreader:
        generacion = pkm["Generation"]
        if generacion in cuenta:
            cuenta[generacion] += 1
        else:
            cuenta[generacion] = 1
    for generacion, total in cuenta.items():
        print(f"Generación {generacion}: {total} pokemons")