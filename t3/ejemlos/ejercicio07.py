def cambiar_vocales(cadena:str)->str:
    ESVOCAL = ("aeiou")
    for i in cadena:
        if i in ESVOCAL:
            i = i.replace(i,"i")
            print(i, end="")
        else:
            print(i, end="")

cambiar_vocales("caseria")
print()

def ninini(cadena: str) -> str:
    ESVOCAL = "aeiouAEIOU" 
    resultado = ""
    for c in cadena:
        if c in ESVOCAL:
            resultado += "i"   # reemplazamos la vocal por 'i'
        else:
            resultado += c     # dejamos el resto igual
    return resultado

print(ninini("gatuno"))  # Salida: cisirii