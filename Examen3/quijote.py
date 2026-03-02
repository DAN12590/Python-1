with open("quijote.txt", encoding="utf8") as quijote:
    ## 1. Cuántas veces sale una palabra pedida al usuario
    a_buscar = input("Palabra a buscar: ")
    contador_palabra = 0
    for linea in quijote:
        ## SUSTITUIR POR SOLUCIÓN
        """if a_buscar in linea.lower():
            contador_palabra += 1"""
        palabras = linea.split()
        for i in palabras:
            if i.lower() == a_buscar:
                contador_palabra += 1
        #verdad 291
        
    print(f"La palabra {a_buscar} aparece {contador_palabra} veces")
    ##

    quijote.seek(0)

    ## 2. Cuántas frases hay
    contador_frases = 0
    for linea in quijote:
        ## SUSTITUIR POR SOLUCIÓN
        for i in linea:
            if i == ".":
                contador_frases += 1
    print(f"Hay {contador_frases} frases")
    ##

    quijote.seek(0)

    ## 3. Contar capítulos
    contador_capítulos = 0
    for linea in quijote:
        ## SUSTITUIR POR SOLUCIÓN
        if ("capítulo") in linea.lower():
            contador_capítulos += 1
        elif ("prólogo") in linea.lower():
            contador_capítulos += 1
    print(f"Hay {contador_capítulos} capítulos")
    ##

    quijote.seek(0)

    ## 4. Palabra más larga
    ## ESCRIBIR SOLUCIÓN
    ##

    mas_larga = ""
    for linea in quijote:
        for palabra in linea.split():
            if len(palabra) > len(mas_larga):
                mas_larga = palabra
    print("La palabra más larga es", mas_larga)


    quijote.seek(0)