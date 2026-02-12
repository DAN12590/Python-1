try:
    n = int(input("Dime un numero: "))
    print(f"El numero al cuadrado es {n ** 2}")
except ValueError as e:
    print("Eso no es un numero")
    