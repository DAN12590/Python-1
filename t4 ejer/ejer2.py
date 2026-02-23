with open("quijote.txt", encoding="UTF8") as archivo:
    quijote = 0
    sancho = 0
    hidalgo = 0
    for linea in archivo:
        for palabra in linea.split():
            if palabra.lower() == "quijote":
                quijote += 1
            if palabra.lower() == "sancho":
                sancho += 1
            if palabra.lower() == "hidalgo":
                hidalgo += 1
    print(quijote, sancho, hidalgo)