with open("quijote.txt", encoding="utf8") as archivo:
    capitulo = None
    for linea in archivo:
        if linea.lower().startswith("capítulo") or linea.lower().startswith("prólogo"):
            if capitulo is not None:
                capitulo.close()
            capitulo = open("Capitulos quijote/" + linea.strip() + ".txt", "w")
        if capitulo is not None:
            capitulo.write(linea)
    capitulo.close()
