with open ("lipsum.txt") as entrada, open ("todo i.txt" , "w") as salida:
    linea = entrada.readline()
    print(linea)
    for linea in entrada: 
        nueva_linea = ""
        for c in linea:
            #if c == "a" or c == "e" or c == "o" or c == "u":
            if c in "aeou":
                nueva_linea += "i"
            #elif c == "A" or c == "E" or c == "O" or c == "U":
            elif c in "AEOU":
                nueva_linea += "I"
            else:
                nueva_linea += c
        salida.write(nueva_linea)