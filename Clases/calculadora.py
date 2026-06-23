operación = str(input("Introduce una operación +, -, *, /: ")) # Lo hago yo, y Python solo compara el string y luego ejecuta el código que YO le he dicho. Compara "+" == + 
num1 = int(input("introduce un número: "))
num2 = int(input("Introduce el segundo número: "))

resultado1 = num1 + num2

resultado2 = num1 - num2

resultado3 = num1 * num2

resultado4 = num1 / num2


def calculadora():
    if operación == "+": 
        print(resultado1)
    elif operación == "-":
        print(resultado2)
    elif operación == "*": 
        print(resultado3)
    elif operación == "/": 
        print(resultado4)

if __name__ == "__main__":
    calculadora()
