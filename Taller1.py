from random import choice
LISTA_PALABRAS = ["patata", "antibiotico", "herencia", "social", "palacio", "biblioteca", "biblioteca", "cerebro", "candado", "escalera"
                  , "equipo", "equipaje", "paciente", "primo", "aspiradora", "trasnochador"]
palabra_aleatoria = choice ( LISTA_PALABRAS )
letras_dichas = []
letras_adivinadas = []
vidas = 5

while vidas>0:

    for i in palabra_aleatoria:
        if i in letras_adivinadas:
            print(i, "", end="")
        else:
            print("_ ", end="")

    letr = input("Adivina una letra o la palabra completa: ")
    letra = letr.lower()
    if letra.isdigit():
        print("No se permiten numeros")
        print("Te quedan", vidas,"vidas")
        print("Letras ya dichas:", letras_dichas)
    else:
        if len(letra) == 1:
            if letra in letras_dichas:
                print("Ya has dicho esta letra")
                print("Te quedan", vidas,"vidas")
                print("Letras ya dichas:", letras_dichas)
            else:
                if letra in palabra_aleatoria:
                    letras_adivinadas.append(letra)
                    print("La letra esta en la palabra")
                    print("Te quedan", vidas,"vidas")
                    print("Letras ya dichas:", letras_dichas)
                else:
                    letras_dichas.append(letra)
                    vidas = vidas - 1
                    print("Te quedan", vidas,"vidas")
                    print("la letra NO esta en la palabra")
                    print("Letras ya dichas:", letras_dichas)
