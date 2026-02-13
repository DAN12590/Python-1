from juego import *
from personajes import *
def jugar():
    print("Bienvenido al juego")
    while True:
        try:
            rondas = int(input("Cuantas rondas quieres jugar? "))
            juego = Juego(rondas)
            break
        except ValueError:
            print("Eso no es un número")
        
    nombree = input("Dime cual es tu nombre: ")

    numclas = 0
    while True:
        numclas = input("Estas son las clases: \n1 => Mago \n2 => Guerrero \n3 => Darkin \nElije que clase quieres: ")
        match numclas:
            case "1":
                print("Has elegido mago")
                pers = juego.nuevo_mago(nombree)
                break
            case "2":
                print("Has elegido guerrero")
                pers = juego.nuevo_guerrero(nombree)
                break
            case "3":
                print("Has elegido Darkin")
                pers = juego.nuevo_darkin(nombree)
                break
            case _:
                print("Opcion no valida, intentelo de nuevo")

    juego.iniciar_juego()

    while juego.ronda <= juego.num_rondas:
        if pers.muerto():
            print("Has muerto")
            break
        print(f"Ronda: {juego.ronda}/{juego.num_rondas}")
        print(f"Estas luchando contra: {juego.get_siguiente()}")
        print(f"Eres {pers}")
        
        accion = 0
        while accion not in ["1", "2"]:
            accion= input(f"Acciones: \n1.Atacar\n2.Curar\nElige: ")
            juego.enemigos[0].atacar(pers)
            match accion:
                case "1":
                    pers.atacar(juego.enemigos[0])
                case "2":
                    pers.curar()
                case _:
                    print("Accion no valida")


        resultado = juego.terminar_ronda()
        if resultado == True:
            print("ENEMIGO VENCIDO")
            juego.ronda += 1
        else: 
            pass
    if juego.final_juego() == True:
        print("HAS GANADO EL JUEGO")

def repetir():
    while True:
        jugar()
        volver_a_jugar = input("¿Quieres volver a jugar? ('s' para sí, cualquier otra tecla para salir): ")
        if volver_a_jugar.lower() != "s":
            print("Hasta pronto, gracias por jugar")
            break
        else:
            continue

repetir()