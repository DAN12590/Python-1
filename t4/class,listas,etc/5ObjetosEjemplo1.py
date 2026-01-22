from math import pi

class Mesa:
    def __init__(self, forma, tamano, material, color):
        self.forma = forma
        self.tamano = tamano
        self.material = material
        self.color = color

    def calcularSuperficie(self):
        if self.forma == "cuadrada":
            return self.tamano ** 2
        elif self.forma == "redonda":
            return pi * (self.tamano ** 2)
mesa1 = Mesa("cuadrada", 150, "madera", "blanca")
mesa2 = Mesa("redonda", 150, "madera", "blanca")
print(f"Mesa {mesa1.forma} de tamaño {mesa1.tamano}")
print(f"Mesa {mesa2.forma} de tamaño {mesa2.tamaño}")