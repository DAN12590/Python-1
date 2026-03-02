from csv import DictReader

def mostrar_pkmn(pkm):
    '''
    Muestra por pantalla la información de un pokemon
    '''
    print(f"Pokemon #{pkm["#"]}: {pkm["Name"]}")
    print(f"- Tipos: {pkm["Type 1"]} {pkm["Type 2"]}")
    print(f"- Generación {pkm["Generation"]}")
    print(f"- Total de stats: {pkm["Total"]}")
    if pkm["Legendary"] == "True":
        print("- Es legendario")

def leer_tipos(csvreader):
    '''
    Obtiene todos los tipos del csv
    '''
    tipos = set()
    for fila in csvreader:
        tipos.add(fila["Type 1"])
    return list(tipos)

def nextono():
    '''
    Permite preguntar al usuario si queremos o no ver el siguiente resultado de una búsqueda
    '''
    nxt = input("Ver siguiente? (q para salir) ")
    if nxt.lower().strip().startswith("q"):
        return True
    return False
            
def buscar_total_superior(csvreader):
    '''
    Visualiza los pokemon cuya columna "Total" es superior a una dada por el usuario
    '''
    supat = int(input("Dime el total que quieres superar: "))
    for pokemon in csvreader:
        total = int(pokemon["Total"])
        if total >= supat:
            mostrar_pkmn(pokemon)
            if nextono():
                return
            
def media_total_legendarios(csvreader):
    total = 0 # Sumamos la columna total
    cuenta = 0 # contamos los legendarios
    for pokemon in csvreader:
        # SUSTITUIR POR SOLUCIÓN
        if pokemon["Legendary"] == "True":
            total += int(pokemon["Total"])
            cuenta += 1
    #print(f"total: {total}, cuenta: {cuenta}")

    print(f"La media es {total / cuenta}")

def gen_con_mas_legendarios(csvreader): # Si quieres puedes hacerlo de otra manera
    cuenta_legendarios = [0, 0, 0, 0, 0, 0] # 6 contadores porque hay 6 generaciones
    for pokemon in csvreader:
        # SUSTITUIR POR SOLUCIÓN
        if pokemon["Legendary"] == "True":
            cuenta_legendarios[int(pokemon["Generation"])- 1] += 1
    print(cuenta_legendarios)
    gen_max = 0
    for i in range(len(cuenta_legendarios)):
        # HALLAMOS EL ÍNDICE DÓNDE ESTÁ EL NÚMERO MÁS ALTO
        if cuenta_legendarios[i] > cuenta_legendarios[gen_max]:
            gen_max = i
    print(f"La generación con más legendarios es {gen_max + 1} que tiene {cuenta_legendarios[gen_max]} legendarios")
            
def ver_megas(csvreader):
    for pokemon in csvreader:
        # SUSTITUIR POR SOLUCIÓN
        if pokemon["Name"] == "Meganium":
            pass
        elif "mega" in pokemon["Name"].lower():
            print(pokemon["Name"])
            
def tipo_mas_comun(csvreader, tipos): # Si quieres puedes hacerlo de otra manera
    cuenta_tipos = dict.fromkeys(tipos, 0)
    contador = {}
    for pokemon in csvreader:
        # SUSTITUIR POR SOLUCIÓN

        if [pokemon["Type 1"]] not in contador:
            contador.append([pokemon["Type 1"]])

        elif pokemon["Type 1"] in contador:
            contador[pokemon["Type 1"]] += 1
    mas_comun = ""
    for i in cuenta_tipos:
        if cuenta_tipos[i] > tipos[mas_comun]:
            mas_comun = i
    print(f"El tipo más común es {mas_comun}")
    print(contador)


## MAIN
with open("pokemon.csv", encoding="utf8") as archivo:
    pokemon = DictReader(archivo)

    tipos = leer_tipos(pokemon)
    archivo.seek(0)
    archivo.readline()

    ## SUSTITUIR ESTO POR EL BUCLE DEL MENÚ

    while True:
        menu = input("""1. Buscar pokemon por total de stats
2. Media de stats totales de los legendarios
3. Generación con mayor número de legendarios
4. Encontrar todos los "megas"
5. Encontrar tipo más común
6. Salir
""")
        match menu:
            case "1":
                buscar_total_superior(pokemon)
                menu = 0
            case "2":
                media_total_legendarios(pokemon)
                menu = 0
            case "3":
                gen_con_mas_legendarios(pokemon)
                menu = 0
            case "4":
                ver_megas(pokemon)
                menu = 0
            case "5":
                tipo_mas_comun(pokemon, tipos)
            case "6":
                break
    ####

    archivo.seek(0)
    archivo.readline()