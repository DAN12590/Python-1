from random import randint
import os
randNum = randint(1, 100)
rondas = 0
campo = ""
punt_mejor = 100

if os.access("puntest.txt",os.F_OK):
    with open ("puntest.txt", "r") as a:
        for linea in a.readlines():
            campo = linea.split(",")
            punt = campo[-1]
            punt = int(punt)
            if punt < punt_mejor:
                punt_mejor = punt

    print("Bienvenido! La mejor puntuación es:", punt_mejor, "y la tiene", campo[0])
else:
    print("Es la primera vez que ejecutas este juego. Bienvenido!")

nombre = input("Introduce tu nombre: ")

while True:
    try:
        rondas += 1
        num = int(input("Introduce un número: "))

        if num > 100 or num < 1:
            print("Debes introducir un número del 1 al 100.")
        else:
            if num > randNum:
                print("Hi")
            elif num < randNum:
                print("Lo")
            else: 
                print("Has ganado con", rondas, "rondas jugadas.")
                with open ("puntest.txt", "a") as a:
                    a.writelines(nombre + "," + str(rondas) + "\n")
                break
    except ValueError:
        print("Eso no es un número")