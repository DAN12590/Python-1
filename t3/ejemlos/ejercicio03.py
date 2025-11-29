def pide_numeros(cantidad_numeros: int) -> int:
    #while cantidad de numeros > 0:
    #   cantidad_numeros -= 1
    lista = []
    for i in range(0, cantidad_numeros):
        num = int(input("Dime un numero(positivo): "))
        lista.append(num)
    return min(lista)

def mi_min(lista):
    ret = lista[0]
    for i in lista[1:]:
        if i < ret:
            ret = i
    return ret

num_min = pide_numeros(5)
print(num_min)

mis_numeros = [5, 3, 8, 2, 7]
min_mio = mi_min(mis_numeros)
print("numero menor es", min_mio)