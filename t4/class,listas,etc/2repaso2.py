from random import randint, choice

ruleta_1 = ["🐒","🗣️","👍","😊","😘","😭"]
ruleta_2 = ["🐒","🗣️","👍","😊","😘","😭"]
ruleta_3 = ["🐒","🗣️","👍","😊","😘","😭"]

def una_vuelta(ruleta):
    una_variable = ruleta[0]
    mi_ruleta = ruleta[1:]
    mi_ruleta.append(una_variable)
    return mi_ruleta

def muchas_vueltas(ruleta, num_vueltas):
    resultado = ruleta
    for i in range(num_vueltas):
        resultado = una_vuelta(resultado)
    return resultado


def dibujar_caja():
    print("╔══════╗")
    for i in range(3):
        print("║" + ruleta_1[i] + ruleta_2[i] + ruleta_3[i] + "║")
    print("╚══════╝")

# ruleta_1 = una_vuelta(ruleta_1)
# ruleta_1 = una_vuelta(ruleta_1)
# ruleta_1 = una_vuelta(ruleta_1)
# ruleta_1 = una_vuelta(ruleta_1)

ruleta_1 = muchas_vueltas(ruleta_1, 4)
dibujar_caja()


'''
    print("Antes de la vuelta", ruleta_1)
    ruleta_1 = una_vuelta(ruleta_1)
    print("Después de la vuelta", ruleta_1)
    ruleta_1 = una_vuelta(ruleta_1)
    print("Después de otra vuelta", ruleta_1)
    '''