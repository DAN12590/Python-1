with open("frases.txt", "w") as archivo:
    lista = []
    lista.append(input("Dime la primera frase: "))
    lista.append(input("Dime la segunda frase: "))
    lista.append(input("Dime la tercera frase: "))
    lista.append(input("Dime la cuarta frase: "))

    for frase in lista:
        print(archivo.write(frase + "\n"))

with open("frases.txt", "r") as archivo:
    for linea in archivo:
        print(linea, end="")