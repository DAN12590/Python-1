try:
    n= int(input("Dime un numero: "))
    print(f"El numero al cuadrado es {n ** 2}")
except ValueError:
    print("Eso no es un número")
finally:
    print("Adios")