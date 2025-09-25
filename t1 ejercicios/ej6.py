a = int(input("dime un numero entero "))

print("multiplo de 5 ", a % 5 == 0)
print("multiplo de 10 ", a % 10 == 0)
if a < 100:
 print("menor que 100")
elif a == 100: 
 print("Igual a 100")
elif a > 100: 
 print("mayor que 100")