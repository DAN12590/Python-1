with open("notas.csv") as archivo_notas:
    archivo_notas.readline()
    susp_tarea1 = 0
    susp_tarea2 = 0
    todo_aprobado = 0
    for linea in archivo_notas:
        campos = linea.split(";")
        nombre = campos[0]
        notas = campos[1:]
        suma = 0
        if int(notas[1]) < 5:
            susp_tarea1 += 1
        if int(notas[2]) < 5:
            susp_tarea2 += 1
        if int(notas[0]) >= 5 and int(notas[1]) >= 5 and int(notas[2]) >= 5 and int(notas[3]) >= 5:
            todo_aprobado += 1
        for nota in notas:
            suma += int(nota)
        print(f"La media de {nombre} es {suma / len(notas)}")
    print(f"Suspensos tarea 1: {susp_tarea1}")
    print(f"Suspensos tarea 2: {susp_tarea2}")
    print(f"Total aprobados: {todo_aprobado}")