class Mascota:
    def __init__(self, nombre, altura, peso):
        self.nombre = nombre
        self.altura = altura
        self.peso = peso

    def hace_ruido(self):
        print(self.nombre, "hace ruido")

    def __str__(self):
        return f"Mascota -> nombre: {self.nombre}, altura: {self.altura}, peso: {self.peso}"

class Perro(Mascota):
    def __init__(self, nombre, altura, peso, raza):
        super().__init__(nombre, altura, peso)
        self.raza = raza
    
    def hace_ruido(self):
        print(self.nombre, "ladra")

class Gato(Mascota):
    pass

mi_mascota = Mascota("Caco", 4, 1000)
mi_mascota.hace_ruido()
mi_perro = Perro("Loki", 0.5, 18, "podenco")
mi_perro.hace_ruido()
print(mi_perro)
mi_gato = Gato("Michi", 30, 15)

if isinstance(mi_perro, Gato):
    print("mi_perro es un gato")
else:
    print("mi_perro no es un gato")

if isinstance(mi_perro, Mascota):
    print("mi_perro es una mascota")
else:
    print("mi_perro no es una mascota")