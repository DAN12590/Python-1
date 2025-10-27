tiempo = 0
hora = 0
tipo = 0

while True: 
    tiempo = input("Introduce el tiempo a convertir ")
    if tiempo.endswith("h"):
        hora = tiempo
        hora = int(hora.replace("h", ""))
        tipo= input("A que quieres convertir (h, m, s)? (q para salir)")
        if tipo == "h":
            print (hora , "h")
        elif tipo == "m":
            print (hora * 60 , "m")
        elif tipo == "s":
            print (hora * 3600 , "s")
        elif tipo == "q":
            break
        else:
            print("Opcion incorrecta")
    elif tiempo.endswith("m"):
        hora = tiempo
        hora = int(hora.replace("m", ""))
        tipo= input("A que quieres convertir (h, m, s)? (q para salir)")
        if tipo == "m":
            print (hora , "m")
        elif tipo == "h":
            print (hora / 60 , "h")
        elif tipo == "s":
            print (hora * 60 , "s")
        elif tipo == "q":
            break
        else:
            print("Opcion incorrecta")
    elif tiempo.endswith("s"):
        hora = tiempo
        hora = int(hora.replace("s", ""))
        tipo= input("A que quieres convertir (h, m, s)? (q para salir)")
        if tipo == "s":
            print (hora , "s")
        elif tipo == "m":
            print (hora / 60 , "m")
        elif tipo == "h":
            print (hora / 3600 , "h")
        elif tipo == "q":
            break
        else:
            print("Opcion incorrecta")