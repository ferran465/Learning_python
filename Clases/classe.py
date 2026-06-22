class programar: 
    def __init__(self, lenguajes): 
        self.lenguajes = lenguajes
        print("Esto es una classe")

    def __str__(self): 
        return self.lenguajes
    
p = programar("Estoy progrmando en python con classes")
print(p)