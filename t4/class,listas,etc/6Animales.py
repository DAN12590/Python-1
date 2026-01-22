class Perros:
    def __init__(self, nombre, raza, edad, altura, peso):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.altura = altura
        self.peso = peso

    def ladrar(self):
        print(self.nombre, ": GUAU")

perro = Perros("Loki", "podenco", 7, .5, 17)
perro.ladrar()
