ALFABETO = "abcdefghijklmnñopqrstuvwxyz"

def cifrar_letra(cadena: str, desfase: int) -> str:
    pos = ALFABETO.find(cadena)
    posN = pos + desfase
    return ALFABETO[posN % len(ALFABETO)]

def cifrar(cadena: str, desfase: int) -> str:
    ret = ""
    for i in cadena:
        ret += cifrar_letra(i, desfase)
    return ret

print(cifrar("abDE", 2))