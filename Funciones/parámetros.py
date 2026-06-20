
cantidad_aceite = int(input("Calcula los ml del aceite: "))
cantidad_vinagre = int(input("Calcula los ml del vinagre: "))

def cocina(aceite, vinagre):

    if aceite == 200:
        print("Su cantidad es exacta")
        return True
    elif aceite > 200:
            print("Se pasa de su cantidad")
            return False

    else:
        if aceite < 200:
            print ("Necesita más cantidad")
            return False
        


    if vinagre == 300: 
        print("Su cantidad es exacta")
        return True
    elif vinagre > 300: 
            print("Se pasa de su cantidad")
            return False
    else: 
        if vinagre < 300: 
             print("Necesita más cantidad")
             return False

cocina(cantidad_aceite, cantidad_vinagre)

