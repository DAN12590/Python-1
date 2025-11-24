def pide_numeros(cantidad_numeros: int) -> int:
    #while cantidad de numeros > 0:
    #   cantidad_numeros -= 1
    lista = []
    for i in range(0, cantidad_numeros):
        num = int(input("Dime un numero(positivo): "))
        lista.append(num)
    return lista

lista_nums = pide_numeros(5)
print(lista_nums)