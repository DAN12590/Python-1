def es_entero(cadena: str) -> bool:
    if (cadena.startswith("+","-")):
        cadena = cadena[1:]
    for i in cadena:
        if i not in "1234567890":
            return False
    return len(cadena) > 0

print(es_entero("1234"))
print(es_entero("12e45"))
print(es_entero(""))
