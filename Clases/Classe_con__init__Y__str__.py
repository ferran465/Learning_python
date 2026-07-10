class programar(): # le decimos con class que haga una classe que se llame programar porque después se crea el objeto programar con p = programar
    def __init__(self, lenguaje): # __init__ necesita que lenguaje tenga un valor ya sea un tipo, string, boleano, lista etc...
        self.lenguaje = lenguaje # con self le decimos que acceda a lenguaje y que se almacene allí en self.lenguaje y tiene que ser = lenguaje porque lo hemos definido arriba
        print("Preparando el objeto")

    def __str__(self): # devuelve un str no lo ejecuta
        return f"Estoy imprimiendo este string {self.lenguaje}" # __str__ solo puede tener el parámetro self porque self se refiere al objeto
                                                                # para después con f"string concatenar el string con la variable

p = programar("python") # a parte de crear el objeto programar assignamos dentro un valor el que sea porque si no __init__ detecta que no tiene ningún valor (TypeError: __init__() missing 1 required positional argument: 'lenguaje')
print(p) # imprimes la variable
