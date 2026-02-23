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
