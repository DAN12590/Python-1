with open("print.txt", "w") as archivo: #abrir el archivo con "w" hace que se sobreescriba todo
    print("Hola todos", file=archivo)