#import
import ejercicio1

def que_mes(num_mes: int) -> str:
    match num_mes:
        case 1:
            return "Enero"
        case 2:
            return "Febrero"
        case 3:
            return "Marzo"
        case 4:
            return "Abril"
        case 5:
            return "Mayo"
        case 6:
            return "Junio"
        case 7:
            return "Julio"
        case 8:
            return "Agosto"
        case 9:
            return "Septiembre"
        case 10:
            return "Octubre"
        case 11:
            return "Noviembre"
        case 12:
            return "Diciembre"
        case _:
            return "No es valido"
     
num_mes = int(input("Que mes quieres saber su equivalencia? "))
print ("tu mes es" , que_mes(num_mes))

#ej como funciona
print ("dime suma ", sum([2, 5]))


# print("tu mes es" ,que_mes(int((input("Que mes quieres saber su equivalencia? ")))))

num_mes = int(input("Que mes quieres saber su equivalencia? "))
resultado = que_mes(num_mes)
print ("tu mes es" , resultado)

#esto es del import
numero = int(input("Dime que numero quieres saber si es par "))
print (es_par(numero))