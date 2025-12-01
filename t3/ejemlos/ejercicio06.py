def invierte_cadena(cadena: str) -> str:
    return cadena[::-1]
def iniverte_cadena_facil(cadena: str) -> str:
    ret = ""
    for i in cadena: #"hola", i = "H", "q", "l", "a"
                     #"H" -> "oH" -> loH
        ret = i + ret #ret + i no invierte nada; solo acumularia la cadena en el mismo orden
    return ret


print(invierte_cadena(input("Dime una cadena: ")))