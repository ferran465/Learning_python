class math: 
    def __init__(self): # Los parámetros pueden ser necesarios si el método los necesita pero si no se pueden crear dentro del método, si no se tienen que crear en el objeto 
        pass
      
    def calculos(self):
        operaciónes = str(input("Introduce una operación +, -, *, /: "))
        num1 = int(input("Introduce un número: "))
        num2 = int(input("introduce el segundo número: "))


        if operaciónes == "+":
                print(num1 + num2)
                return num1 + num2
        elif operaciónes == "-":
                print(num1 - num2)
                return num1 - num2
        elif operaciónes == "*":
                print(num1 * num2)
                return num1 * num2
        elif operaciónes == "/":
                print(num1 / num2)
                return num1 / num2

if __name__ == "__main__": 
    c = math()
    print("Math")

