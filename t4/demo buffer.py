with open("buffer.txt", "w") as archivo:
    for i in range(10):
        print("El numero es", i , file=archivo, flush=True)
        archivo.flush() #Este método vacía el buffer de salida y escribe lo que está almacenado en el buffer en el archivo.
        input("Enter para continuar")

"""A veces, cuando escribes en un archivo, 
los datos no se escriben de inmediato, 
sino que se mantienen en un buffer y se vacían cuando
 el buffer está lleno o cuando el programa termina. Usar 
 flush=True hace que Python vacíe el buffer y escriba en el archivo en 
 ese momento, asegurando que los datos se guarden inmediatamente."""