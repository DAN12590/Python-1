with open("writelines.txt", "w") as archivo:
    lista = ["Hola", "Como", "Estas"] 
    archivo.writelines(lista) #Necesitas controlar el formato (como agregar saltos de línea \n) manualmente