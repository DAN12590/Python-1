_PREC = 1e-15
_ITE_MAX = 10000000

# TODO Devuelve el valor absoluto de un número
# es decir, le quita el signo a los negativos
def abs(num: float) -> float:
    if num<0:
        return num * -1
    else:
        return num

# TODO Devuelve el número más pequeño de los dos
def min(num1: float, num2: float) -> float:
    if num1 < num2:
        return num1
    elif num2< num1:
        return num2

# TODO Devuelve el número más grande de los dos
def max(num1: float, num2: float) -> float:
    if num1 > num2:
        return num1
    elif num2> num1:
        return num2

# No tocar, pow(a, b) calcula a elevado a b
# sqrt calcula la raiz cuadrada de un número
def pow(a: float, b: float) -> float:
    return a ** b

def sqrt(numero: float) -> float:
    app = numero / 2
    ite = 0
    while abs(app * app - numero) > _PREC and ite < _ITE_MAX:
        app = app - (app * app - numero) / (2 * app)
        ite += 1
    return app

####

# TODO Devuelve True si a² + b² = c²
def terna_pit(a: int, b: int, c: int) -> bool:
    if pow(a, 2) + pow(b, 2) == pow(c, 2):
        return True
    else:
        return False

# TODO Muestra mediante un print todas las ternas que cumplen lo de antes
def ternas_hasta(max: int):
    for i in range(1, max):
        for j in range(1, max):
            for k in range(1, max):
                if terna_pit(i, j, k) == True:
                    print(i , j, k)
                else:
                    pass

if __name__ == "__main__":
    print(sqrt(9))
    print(abs(-53.32))
    print(min(2,7), "es mas pequeño")
    print(max(4,36), "es mas grande")
    print(terna_pit(3,4,5), " verdad a² + b² = c²")
    print(terna_pit(8,4,5), "falso a² + b² = c²")
    ternas_hasta(22)
