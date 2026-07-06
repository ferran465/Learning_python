def dividir():
    try:
        a = int(input("Introduce el dividendo: "))
        b = int(input("Introduce el divisor: "))
        return a / b
    except ZeroDivisionError as z:
        print("0/0 no és válido")
        return z
    except ValueError as v:
        print("El número introducido no és válido")
        return v
print(dividir())
