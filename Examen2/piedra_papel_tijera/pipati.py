from random import choice
# TODO devuelve 1 si gana op1, 2 si gana op2 y 0 si es un empate
# op1 puede ser "piedra", "papel" o "tijera"
def quien_gana(op1: str, op2: str) -> int:
    op1 = op1.lower()
    op2 = op2.lower()
    if op1 == op2:
        return (0)
    if op1 == "tijera" and op2 == "papel":
        return (1)
    if op1 == "papel" and op2 == "piedra":
        return (1)
    if op1 == "piedra" and op2 == "tijera":
        return (1)
    if op2 == "tijera" and op1 == "papel":
        return (2)
    if op2 == "papel" and op1 == "piedra":
        return (2)
    if op2 == "piedra" and op1 == "tijera":
        return (2)

# TODO arreglar
def verifica_entrada(opcion: str) -> bool:
    if opcion in ["piedra", "papel", "tijera"]:
        return True
        #return opcion.lower() in ["Piedra", "Papel", "Tijera"]
    else:
        return False


# Este funcionará cuando arregles el de arriba
def pedir_opcion() -> str:
    op = ""
    while not verifica_entrada(op):
        op = input("¿Qué juegas? (piedra, papel, tijera): ")
        if not verifica_entrada(op):
            print("Opción incorrecta")
    return op

# No tocar
def ordenador_elige() -> str:
    return choice(["piedra", "papel", "tijera"])

def main():
    print("=*=*=*= PIEDRA PAPEL TIJERA =*=*=*=")
    victorias_comp = 0 # Cuántas veces ha ganado el ordenador
    victorias_juga = 0 # Cuántas veces ha ganado el jugador
    rondas_max = int(input("¿Cuántas rondas hay que ganar? "))

    while victorias_comp < rondas_max and victorias_juga < rondas_max:
        # TODO en cada ronda, pedimos al jugador entrada usando pedir_opcion()
        # después, el ordenador elige aleatoriamente su opción con ordenador_elige()
        # Determinamos quién gana con quien_gana e incrementamos el contador correspondiente
        res1 = pedir_opcion()
        res2= ordenador_elige()
        print("El ordenador elige: ",res2)
        if quien_gana(res1,res2) == 1:
            victorias_juga += 1
            print("Jugador: ",victorias_juga,"Computadora: ", victorias_comp)
        elif quien_gana(res1,res2) == 2:
            victorias_comp += 1
            print("Jugador: ",victorias_juga,"Computadora: ", victorias_comp)
        elif quien_gana(res1,res2) == 0:
            print("Jugador: ",victorias_juga,"Computadora: ", victorias_comp)
            continue
        

    # TODO muestra quién ha ganado al final
    if victorias_juga > victorias_comp:
        print("Ha ganado el jugador")
    elif victorias_juga < victorias_comp:
        print("Ha ganado la computadora")

if __name__ == "__main__":
    main()
'''

res1="a"
res2= ordenador_elige()
res1 = input("(jugador1) piedra, papel o tijera: ")
print(verifica_entrada(res1))

print(res1)
print(res2)
print(quien_gana(res1,res2))
'''