with open("quijote.txt", encoding="UTF8") as archivo:
    mas_larga = ""
    for linea in archivo:
        for palabra in linea.split():
            if len(palabra) > len(mas_larga):
                mas_larga = palabra
    print("La palabra mas larga es: ", mas_larga)