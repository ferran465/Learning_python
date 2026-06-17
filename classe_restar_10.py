class restar_10: 
    def __init__(self, restar): 
        self.restar = restar
        print("resta diez")


    def __str__(self):
        return f"Esto resta diez {self.restar}"

if __name__ == "__main__": # Lo que hace __name__ es usar una étiqueta para classificar si el archivo es principal o no para que python pueda ejecutarlo o importarlo i "__main__" se guarda dentro de __name__ y se classifica entonces python puede decidir si importar o ejecutar.
    r = restar_10(- 10)    # Python decide si el archivo se ejecuta o se importa y asigna a __name__ el valor "__main__" (__name__ = "__main__") o el nombre del archivo.
        