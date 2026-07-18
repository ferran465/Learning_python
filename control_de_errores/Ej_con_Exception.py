def leer_numero_de_archivo(ruta):
    try:    
        with open(ruta, "r") as f:
            contenido = f.read()
        numero = int(contenido)
        return numero * 2

    except FileNotFoundError as l:
        print("No se ha encontrado el archivo", l)
        return
    
    except ValueError as s:
        print("Esto no es un valor válido", s)
        return None
    
    
    except Exception as p:
        print("Error inesperado", p)
        return None
    
print(leer_numero_de_archivo(ruta = "contenido"))
    


    # El programa intenta convertir el texto a número. Si lo consigue, ahí tienes el número. Si no lo consigue, en ese mismo intento salta el ValueError.