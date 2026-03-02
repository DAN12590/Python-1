import random as r

NOMBRES = "Pepe Lucía Juan Jaime Eduardo Lucas Laura Raquel Diego Rita".split()
APELLIDOS = "Pérez Gómez Rodríguez López Palacios García Artal Talavera".split()

nombres_generados = []


def nom_aleatorio():
    return r.choice(NOMBRES) + " " + r.choice(APELLIDOS) + " "\
                + r.choice(APELLIDOS)


with open("notas.csv", "w") as f:
    print(";".join(["Alumno", "Examen 1", "Tarea 1", "Tarea 2", "Examen 2"]),
          file=f)
    for i in range(50):
        nombre = nom_aleatorio()
        while nombre in nombres_generados:
            nombre = nom_aleatorio()
        nombres_generados.append(nombre)
        print(nombre, end="", file=f)
        print(";" + ";".join([str(int(r.random() * 11)) for i in range(4)]), file=f)
