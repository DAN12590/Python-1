import random

class Personaje:
    def __init__(self, vida_inicial, ataque, defensa, nombre):
        self.vida = vida_inicial
        self.vida_inicial = vida_inicial
        self.ataque = ataque
        self.defensa = defensa
        self.nombre = nombre

    def atacar(self, otro):
        otro.vida -= 0 if ( self.fuerza - otro.defensa ) < 0 else self.fuerza - otro.defensa
    
    def curar(self):
        pass

    def reset(self):
        self.vida = self.vida_inicial

    def muerto(self):
        if self.vida <= 0:
            return True
        else:
            return False
        
    def __str__(self):
        return (f"{self.nombre} => VIDA: {self.vida}/{self.vida_inicial}")
#personaje
# pers=Personaje("120", "20", "10", "pepe"); print(pers)


class Mago(Personaje):
    FUERZA_MAGIA = 20
    FUERZA_SIN_MAGIA = 5
    DEFENSA = 5
    MANA_INICIAL = 10

    def __init__(self, vida_inicial, nombre):
        super().__init__(vida_inicial, Mago.FUERZA_MAGIA, Mago.DEFENSA, nombre)
        self.mana = self.MANA_INICIAL
    
    def reset(self):
        super().reset()
        self.mana = Mago.MANA_INICIAL
        self.ataque = Mago.FUERZA_MAGIA

    def __str__(self):
        return super().__str__() + f"; Mana: {self.mana}"

    def atacar(self, otro):
        if self.mana > 0:
            self.mana -= 1
            otro.vida -= Mago.FUERZA_MAGIA
        else:
            otro.vida -= Mago.FUERZA_SIN_MAGIA
    
    def curar(self):
        if self.mana > 0:
            self.mana -= 1
            self.vida += Mago.FUERZA_MAGIA
            if self.vida > self.vida_inicial:
                self.vida = self.vida_inicial
        else:
            "no hay mana"

# mago  
# m = Mago("Gandalf", 150); print (m)

#probar curar mago
# m = Mago("Gandalf", 150); print(m); m.vida = -1000; print(m); m.curar(); print(m); m.curar(); print(m); m.reset(); print(m)

class Guerrero(Personaje):
    FUERZA = 15
    DEFENSA = 10
    POCIONES_INICIAL = 2

    def __init__(self, vida_inicial, nombre):
        super().__init__(vida_inicial, Guerrero.FUERZA, Guerrero.DEFENSA, nombre)
        self.pociones = self.POCIONES_INICIAL

    def curar(self):
        if self.pociones >= 1:
            self.vida = self.vida_inicial
            self.pociones -= 1
        
    def reset(self):
        super().reset()
        self.pociones = self.POCIONES_INICIAL

    def __str__(self):
        return super().__str__() + f"; Pociones: {self.pociones}"


# g = Guerrero("Paco", 200)
# curar Guerrero
#print(g); g.vida = 50; print(g); g.curar(); print(g); g.vida = 50; print(g); g.curar(); print(g); g.vida = 50; print(g); g.curar(); print(g)

class Enemigo(Personaje):
    VIDA_INICIAL = random.randint(20, 100)
    FUERZA = random.randint(2, 10)
    DEFENSA = random.randint(1, 3)
    def __init__(self, nombre):
        super().__init__(Enemigo.VIDA_INICIAL, Enemigo.FUERZA, Enemigo.DEFENSA, nombre)

#Esto es lo pone pero lo pongo para guiarme
    def __str__(self):
        return super().__str__() + f"; Ataque: {self.ataque} ; Defensa: {self.defensa}"
    
#enem = Enemigo("sebas")
#print(enem)