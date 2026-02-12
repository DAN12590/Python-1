while True:
    try:
        n= int(input("Dime un numero: "))
        print(f"El numero al cuadrado es {n ** 2}")
        break
    except ValueError:
        print("Eso no es un número")