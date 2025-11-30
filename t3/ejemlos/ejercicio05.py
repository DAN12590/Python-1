
'''
def dibuja_cuadrado_py(lado: int):
    print((("#"* lado)+ "\n")* lado)
'''
'''
def dibuja_cuadrado_medio(lado: int):
    for i in range(lado):
        print("#" * lado)
'''
def dibu_cuadrado(lados: int):
    for i in range(lados):
        for j in range(lados):
            print("#", end="")
        print()
 
dibu_cuadrado(int(input("Dime los lados del cuadrado ")))
#el print() solo inserta un salto de linea

# dibuja_cuadrado_py(6)
# dibuja_cuadrado_medio(7)