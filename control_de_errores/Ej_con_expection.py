def leer_config(ruta):
    try:
        archivo = open(ruta)
        contenido = archivo.read()
        numero = int(contenido)
        archivo.close()
        return numero
    except ValueError:
        print("no és un número válido")
    except FileNotFoundError:
        print("Este archivo no existe")

leer_config("config.txt")