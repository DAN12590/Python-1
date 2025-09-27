import math

cateto1 = float(input("Longitud primer cateto "))
cateto2 = float(input("Longitud segundo cateto "))

hipot1 = (cateto1**2 + cateto2**2)**0.5

hipot2 = math.sqrt(cateto1**2 + cateto2**2)

print("la hipotenusa es ", hipot1)
print("la hipotenusa es ", hipot2)