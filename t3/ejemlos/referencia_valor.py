a = 9
l1 = [1, 5, 7, 3]

b = a
b += 5
print("a =", a)
print("b =", b)


def annade(lista, elemento):
    lista.append(elemento)

l1 = [1, 2, 3, 4]
annade(l1, 5)
print(l1)