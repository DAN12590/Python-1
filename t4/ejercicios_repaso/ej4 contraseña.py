with open("contraseña.txt", "w") as archivo:
    archivo.write(input("Dime la contraseña a poner: "))

    contrasena_user = ""

with open("contraseña.txt", "r") as archivo:
    contrasena_real = archivo.read().strip()
    while contrasena_real != contrasena_user:
        contrasena_user = input("Dime la contraseña para continuar: ")
        if contrasena_real == contrasena_user:
            print("Contraseña correcta")
            break
        else:
            print("Contraseña incorrecta")

