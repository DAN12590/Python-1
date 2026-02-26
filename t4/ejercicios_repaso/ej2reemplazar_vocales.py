with open("quijote.txt", encoding="UTF8") as archivo:
    with open("quijote_modificado.txt", "w", encoding="UTF8") as salida:
        for linea in archivo:
            nueva_linea = ""
            for c in linea:
                if c in "aeiou":
                    nueva_linea += "*"
                else:
                    nueva_linea += c
            salida.write(nueva_linea)