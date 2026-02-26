with open("quijote.txt", encoding="UTF8") as archivo:
    palabra = input("Dime la palabra que quieres que busque: ")
    contador = 0
    for lineas in archivo:
        if palabra in lineas.lower():
            contador += 1

print(palabra)
print(contador)