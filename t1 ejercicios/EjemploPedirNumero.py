while True:
    num = input("Introduce un numero: ") 

    if num.isdecimal() or num.startswith("-") and num [1:].isdecimal():
        num = int(num)
        break
    else:
        print("No es un numero")
print(num + 5)