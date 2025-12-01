def esta_ordenada(lista):
    for i in range (len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True

def swap_short_vuelta(lista):
    ret = lista.copy()
    for i in range(len(ret) - 1):
        if ret[i] > ret [i + 1]:
            aux = ret[i]
            ret[i] = ret [i + 1]
            ret[i + 1] = aux
    return ret

def swap_short_vueltas(lista):
    ret = lista.copy()  # Creamos una copia de la lista para no modificar la original
    while not esta_ordenada(ret):  # Mientras la lista no esté ordenada
        for i in range(len(ret) - 1):  # Recorremos la lista
            if ret[i] > ret[i + 1]:  # Si el elemento actual es mayor que el siguiente
                # Intercambiamos los elementos
                aux = ret[i]
                ret[i] = ret[i + 1]
                ret[i + 1] = aux
    return ret  # Devolvemos la lista ordenada

print(swap_short_vuelta([2,5,7,3,1]))
    
print(esta_ordenada([1,2,3,4,5,6]))
print(esta_ordenada([2,5,7,3,1]))
print(swap_short_vuelta([2,5,7,3,1]))
print(swap_short_vueltas([2,5,7,3,1]))