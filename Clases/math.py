class calculadora: 
    def __init__(self, sumar, restar, multiplicar, dividir, operaciones):
        self.sumar = sumar
        self.restar = restar
        self.multiplicar = multiplicar
        self.dividir = dividir
        self.operaciones = operaciones
        print("Estás són las operaciónes")
    def calculadora(self):
        operaciónes = str(input("Introduce una operación: "))
        num1 = int(input("Introduce un número: "))
        num2 = int(input("introduce el segundo número:"))

        self.sumar = num1 + num2
        self.restar = num1 - num2 
        self.multiplicar = num1 * num2
        self.dividir = num1 / num2

if __name__ == "__main__": 
    c = calculadora(0, 0, 0, 0, None)
    print("Math")
else: 
    print (None)