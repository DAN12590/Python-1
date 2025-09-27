import math
radio = float(input("Dime el radio de la circunferencia en cm "))

perimetro = radio * 2 * math.pi
area = radio**2 * math.pi

print ("El perimetro de la circunferencia es", perimetro, "cm")
print ("El area de la circunferencia es ", area, "cm²")