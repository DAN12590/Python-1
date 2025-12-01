# TODO importamos el módulo mates
from mates_modulo.mates import *

def main():
    opcion = 0
    while opcion != 4:
        print("Calculadora avanzada:")
        print("1. Elevar un número a otro")
        print("2. Raiz cuadrada")
        print("3. Ver ternas pitagóricas")
        print("4. Salir")
        opcion = int(input("Elige una opción>>> "))

        # TODO Completa la expresión match usando funciones de mates_modulo.mates
        match opcion:
            case 1:
                num1= int(input("Elige el numero: "))
                num2= int(input("Dime a cuanto lo elevo: "))
                print("El resultado es: ", pow(num1,num2))
            case 2:
                num1= int(input("Elige el numero: "))
                print("La raiz cuadrada de",num1,"es: ", sqrt(num1) )
            case 3:
                num1= int(input("Elige el numero: "))
                print(ternas_hasta(num1))
            case 4:
                print("Saliendo")
                break
            case _:
                print("Opción incorrecta")

if __name__ == "__main__":
    main()
