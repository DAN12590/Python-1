with open("archivo.txt", "w") as archivo:
    archivo.write("Hola Mundo")  #no agrega una nueva línea automáticamente

with open("archivo.txt", "w") as archivo:
    archivo.write("Adiós Mundo") #Si escribes de nuevo con write(), sobrescribirá el contenido anterior