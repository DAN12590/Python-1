class Coche:
    def __init__(self, marca, modelo, matricula, vel_punta):
        self.marca = marca
        self.modelo = modelo
        self.matricula = matricula
        self.vel_punta = vel_punta
        self.vel_actual = 0
    
    def acelerar(self, incremento):
        vel_obj = self.vel_actual + incremento
        if vel_obj > self.vel_punta:
            self.vel_actual = self.vel_punta
        else:
            self.vel_actual = vel_obj

    def frenar(self, decremento):
        vel_objeto = self.vel_actual - decremento
        if vel_objeto < 0:
            self.vel_actual = 0
        else:
            self.vel_actual = vel_objeto

mi_coche = Coche("SEAT", "Mii", "1234XYZ", 180)
print("La marca del coche es", mi_coche.marca)
mi_coche.marca = "Skoda"
print("La marca del coche es", mi_coche.marca)
print("La velocidad del coche es", mi_coche.vel_actual)
mi_coche.acelerar(350)
print("La velocidad del coche es", mi_coche.vel_actual)
print("La velocidad maxima del coche es", mi_coche.vel_punta)
mi_coche.frenar(30)
print("La velocidad del coche es", mi_coche.vel_actual)
mi_coche.frenar(200)
print("La velocidad del coche es", mi_coche.vel_actual)