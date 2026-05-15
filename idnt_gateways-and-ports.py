eleccion = int(input("Elige una puerta: " ))

valor = float(input("Elige un valor: "))

Acceso_Negativo = "No puedes acceder"

Acceso_Positivo = "puedes acceder"



def puerta1(): 
      
    if eleccion == 1: 
        if valor <= 10:     # El valor puede ser igual o menor
            print(Acceso_Positivo)
        else: 
            if valor >10:
                print(Acceso_Negativo)

puerta1()

    
    
def puerta2():    
    if eleccion == 2:                   
        if valor <= 20:      # El valor puede ser igual o menor 
            print(Acceso_Positivo)
        else: 
            if valor >20:
                print(Acceso_Negativo)

puerta2()


def puerta3():
    if eleccion == 3: 
        if valor <= 30:      # El valor puede ser igual o menor
            print(Acceso_Positivo)
        else: 
            if valor >30:
                print(Acceso_Negativo)


puerta3()


            





    