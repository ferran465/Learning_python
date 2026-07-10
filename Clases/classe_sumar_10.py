class sumar_10: 
    def __init__(self, sumar):
        self.sumar = sumar 
        print("suma diez")

    def __str__(self): # __str__ solo puede tener el parámetro self porque self se refiere al objeto
        return f"Esto suma diez {self.sumar}"
        
if __name__ == "__main__":
    s = sumar_10(+ 10)
    print(s)

