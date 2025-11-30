def es_par(num1) -> bool:
    if num1 % 2 == 0:
        return True
    else:
        return False

numero = int(input("Dime que numero quieres saber si es par "))
print (es_par(numero))