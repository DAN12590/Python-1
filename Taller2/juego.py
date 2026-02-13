from random import randint
from personajes import *

class Juego:
    NOMBRES = ["Aragorn", "Elena", "Draknar", "Morgana", "Zara", "Thalion", "Eldric", "Seraphine", "Vornak", "Isolde"]
    def __init__(self, num_rondas):
        self.num_rondas = num_rondas
        self.enemigos = []
        self.jugador = None
        self.ronda = 1

    def iniciar_juego(self):
        self.enemigos = []
        self.ronda = 1
        for i in range(self.num_rondas):
            """
            self.enemigos.append(Juego.NOMBRES[random.randint(0, 9)])
           """
            nombre_enemigo = Juego.NOMBRES[random.randint(0, 9)]
            enemigo = Enemigo(nombre_enemigo)
            self.enemigos.append(enemigo)
            

    def get_siguiente(self):
        return self.enemigos[0]

    def terminar_ronda(self) -> bool:
        if self.enemigos[0].vida <= 0:
            self.enemigos.pop(0)
            return True
        else:
            return False

    def nuevo_guerrero(self, nombre):
        guerrero = Guerrero(randint(100, 200), nombre)
        self.jugador = guerrero
        return guerrero 

    def nuevo_mago(self, nombre):
        mago = Mago(randint(50, 150), nombre)
        self.jugador = mago 
        return mago

    def nuevo_darkin(self, nombre): 
        darkin = Darkin(randint(100, 150), nombre)
        self.jugador = darkin
        return darkin

    def final_juego(self):
        if self.enemigos == []:
            return True


"""jue = Juego(5)
jue.iniciar_juego()
print(jue.enemigos)
print(jue.get_siguiente())
print(jue.enemigos)
print(jue.terminar_ronda())
jue.get_siguiente().vida = 20
print(jue.get_siguiente().vida)"""