import random
from personajes import *

class Juego:
    NOMBRES = ["Aragorn", "Elena", "Draknar", "Morgana", "Zara", "Thalion", "Eldric", "Seraphine", "Vornak", "Isolde"]
    def __init__(self, num_rondas):
        self.num_rondas = num_rondas
        self.enemigos = []
        self.jugador = None
        self.ronda = 0

    def iniciar_juego(self):
        self.enemigos = []
        self.ronda = 0
        for i in range(self.num_rondas):
            """
            self.enemigos.append(Juego.NOMBRES[random.randint(0, 9)])
           
            (PREGUNTAR DIEGO COMO DAR CARACTERISTICAS de Enemigo a los enemigos)"""
            nombre_enemigo = Juego.NOMBRES[random.randint(0, 9)]
            enemigo = Enemigo(nombre_enemigo)
            self.enemigos.append(enemigo)
            

    def get_siguiente(self):
        return self.enemigos[0]

    def terminar_ronda(self):
        if Enemigo.vida == 0:
            self.enemigos.pop(0)



jue = Juego(5)
jue.iniciar_juego()
print(jue.enemigos)
print(jue.get_siguiente())
print(jue.enemigos)
