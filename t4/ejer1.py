from random import randint
from os import access, F_OK

ARCHIVO = "puntuaciones.txt"

def pedir_numero():
    try:
        num = int(input("Dime un numero del 1 al 100: "))
        if 100 >= num >= 1:
            return num
        else:
            print("Tiene que estar entre el 1 y el 100 ")
    except ValueError:
        print("No es un numero valido")

def archivo_existe():
    return access(ARCHIVO, F_OK)
#Esta función usa access() para verificar si el archivo puntuaciones.txt 
#existe en el sistema. Si el archivo existe, devuelve True; si no, devuelve False

def sacar_puntuacion():
    with open(ARCHIVO) as puntuaciones:
        contenido = puntuaciones.read()
        partida = contenido.split()
        partida[1] = int(partida[1])
        return partida
    
def almacenar_puntuacion(puntos):
    with open(ARCHIVO, "w") as puntuaciones:
        nombre = input("Dime tu nombre: ")
        print(f"{nombre}{puntos}", file=puntuaciones)

print("Vamos a jugar al HiLo")
if archivo_existe():
    contenido = sacar_puntuacion()
    nombre = contenido[0]
    puntos_max = contenido[1]
    print(f"El record lo tiene {nombre} y es {puntos_max}")

num_aleatorio = randint(1, 100)
intentos = 0
while True:
    num = pedir_numero()
    intentos += 1
    if num > num_aleatorio:
        print("Hi")
    elif num < num_aleatorio:
        print("Lo")
    else:
        print(f"Has ganado en {intentos} intentos")
        if puntos_max is None or intentos < puntos_max:
            almacenar_puntuacion(intentos)
        break