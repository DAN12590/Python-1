class Vehiculo:
    def __init__(self, marca, matricula, color, motor):
        self.marca = marca
        self.matricula = matricula
        self.color = color
        self.motor = motor
        self.velocidad = 0
    
    def acelerar(self, incremento):
        self.velocidad += incremento
    
    def frenar(self, decremento):
        self.velocidad -= decremento

    def __str__(self):
        return f"Vehiculo -> Marca {self.marca}, matricula {self.matricula}" \
                + f", color {self.color}, motor {self.motor}"

class Coche(Vehiculo):
    def __init__(self, marca, matricula, color, motor, num_puertas):
        super().__init__(marca, matricula, color, motor)
        self.num_puertas = num_puertas
    
    def __str__(self):
        super_str = super().__str__()
        return "Coche: " + super_str + ", número puertas " + str(self.num_puertas)

class Moto(Vehiculo):
    def __init__(self, marca, matricula, color, motor, num_ruedas):
        super().__init__(marca, matricula, color, motor)
        self.num_ruedas = num_ruedas

    def __str__(self):
        super_str = super().__str__()
        return "Moto: " + super_str + f", número ruedas {self.num_ruedas}"
    
    def encuentra_matricula(slef, matricula):
        pass

class Concesionario:
    def __init__(self):
        self.lista_vehiculos = []

    def annade_vehiculo(self,vehiculo):
        self.lista_vehiculos.append(vehiculo)

    def mostrar_vehiculos(self):
        for i in self.lista_vehiculos:
            print (i)
    
    def encuentra_vehiculo(self, matricula):
        for vehiculo in self.lista_vehiculos:
            if vehiculo.matricula == matricula:
                return vehiculo
        else:
            return None
    
    def vender_vehiculo(self, matricula):
        '''
        Docstring for vender_vehiculo

        :param self: Description
        :param matricula: La matrícula del vehículo a eliminar
        Devuelve True si conseguimos eliminar de la lista el vehículo
        False si no lo eliminamos (si no existe)
        '''
        for i in range(len(self.lista_vehiculos)):
            pass


conc = Concesionario()
conc.annade_vehiculo(Coche("SEAT", "1234XYZ", "Blanco", "IL4", 5))
conc.annade_vehiculo(Moto("Honda", "4567ZWF", "Roja", "500cc", 2))

print(conc.encuentra_vehiculo("1234XYZ"))
print(conc.encuentra_vehiculo("1234XYW"))

if not conc.encuentra_vehiculo("1234XYW"):
    print("El vehiculo existe")
else:
    print("El vehiculo existe")
conc.mostrar_vehiculos()
conc.vender_vehiculo ("1234XYZ")
conc.mostrar_vehiculos()
