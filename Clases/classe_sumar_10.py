class sumar_10: 
    def __init__(self, sumar):
        self.sumar = sumar 
        print("suma diez")

    def __str__(self):
        return f"Esto suma diez {self.sumar}"
        
if __name__ == "__main__":
    s = sumar_10(+ 10)
    print(s)

