try:
    cantidad_aceite = int(input("Calcula los ml del aceite: "))
    cantidad_vinagre = int(input("Calcula los ml del vinagre: "))
except:
    print ("solo se pueden escribir números")
     


    def cocina(aceite, vinagre):

        if aceite == 200:
            print("Su cantidad es exacta")
            return True
        else: 
            if aceite > 200:
                print("Se pasa de su cantidad")
                return False
            


        if vinagre == 300: 
            print("Su cantidad es exacta")
            return True
        else: 
            if vinagre > 300: 
                print("Se pasa de su cantidad")
                return False
            
            

    cocina(cantidad_aceite, cantidad_vinagre)