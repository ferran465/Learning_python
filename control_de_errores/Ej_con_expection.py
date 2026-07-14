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

leer_config(ruta="config.txt")

# leer_config(ruta="config.txt")

# Sirve para identificar claramente qué valor corresponde a cada parámetro, algo más útil cuantos más parámetros tenga la función, porque a simple vista se vuelve difícil recordar el orden correcto.

