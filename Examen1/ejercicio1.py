print("Bienvenido al programa que nos va a decir si podemos ganar una partida de dardos en un único dardo")
faltan = int(input("Dime cuantos puntos te quedan para ganar "))

if faltan >= 1 and faltan <= 20:
    print ("Apuntar a zona de numeros directamente")
elif faltan % 2 == 0 and faltan <= 40:
    print ("Apuntar a la zona doble")
elif faltan %3 == 0 and faltan <= 60:
    print ("Apuntar a la zona triple")
elif faltan == 25:
    print ("Apuntar a la zona BULL")
elif faltan == 50:
    print("Aputnar a la zona doble BULL")
else:
    print ("No puedes ganar con un solo dardo")