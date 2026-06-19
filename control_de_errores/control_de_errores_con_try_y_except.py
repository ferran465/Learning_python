def Errores():
    try: 
        Error_nº1 = int(input("Introduce un valor igual o más alto que 1000: "))
        if Error_nº1 == 1000: 
            print("Bien")
            return True 
        else: 
            print("Error")
            return False

    except: 
        print("debes introducir un numero")
        return False
    
print(Errores())