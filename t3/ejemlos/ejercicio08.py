def media(lista):
    suma = 0
    for i in lista:
        suma = suma + i
    return suma / len(lista)

print(media([1, 4, 5, 8, 2]))

def media1(numeros: list)->float:
    cantidadnum = len(numeros)
    return sum(numeros)/cantidadnum
    #return sum(numeros) / len(numeros)      (en vez de los 2 de arriba)


nume = [1 ,2 ,5 ,8 ,6, 3]
print(media1(nume))