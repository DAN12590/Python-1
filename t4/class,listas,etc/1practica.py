from random import randint

def palmamos() -> bool:
    num_aleatorio = randint(0,5)
    return num_aleatorio == 0

def recargar(tambor, num_balas):
    while sum(tambor) < num_balas:
        sitio_aleatorio = randint(0, len(tambor) -1 ) 
        tambor [sitio_aleatorio] = 1    

def disparar(tambor):
    ret = tambor[0]
    del tambor[0]
    return ret
vidas = 3
puntos = 0
num_max = 0
pasar = 1
tambor = [0,0,0,0,0,0]
while vidas >= 0:
    if tambor == []:
        tambor = [0,0,0,0,0,0]
        recargar(tambor, 3)
    print(tambor)
    print("Te quedan ",vidas,"vidas")
    print("Has sobrevivido ", puntos,"rondas")
    print("Puedes pasar ", pasar,"veces")
    juega = input("Quieres jugar? (si,no) ")
    if juega == "si":
        if disparar(tambor):
            print("Palmas")
            vidas -= 1
        else:
            puntos+= 1
            print("Vives para ver otro dia")
    else:
      if pasar > 0:
        puntos += 1
        if disparar(tambor) == 1:
            print("BANG")
        else: 
            print("Click")

