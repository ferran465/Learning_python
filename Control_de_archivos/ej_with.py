
def write_archivo():
    with open("archivo.txt", "w") as archivo:
        archivo.write("Hello, World")

    with open("archivo.txt", "r") as archivo: 
        contenido = archivo.read()
        print(contenido)
        return contenido
       

write_archivo()