def ejercicio_with(): 
    with open ("archivo1", "w") as archivo: 
        archivo.write("Hola, mundo" "\n")
        archivo.write("Hello, World" "\n")
        archivo.write("Hello Friend" "\n")

    
    with open ("archivo1", "r") as archivo: 
        contenido = archivo.read()
        return contenido
    
print(ejercicio_with())
