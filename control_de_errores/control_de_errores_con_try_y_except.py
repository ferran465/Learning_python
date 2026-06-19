Error_nº1 = int(input("Introduce un valor igual o más alto que 1000: "))

def Errores():
    try: 
        if Error_nº1 == 1000: 
            print("Bien")
            return True 
        
    except Error_nº1 as error:
        if Error_nº1 > 1000: 
            return False

print(Errores())
        