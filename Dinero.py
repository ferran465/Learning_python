dinero1 = float (input("Introduce una cifra de dinero: "))

mayor_cantidad = "Solo puede introducir 5 o igual"

cantidad_normal = "su cantidad és exacta"

def dinero():
        if dinero1 >=5:
            print(cantidad_normal)

        else: 
            if dinero1 <5:
                for i in range(0, 4):
                    if dinero1 == i:
                        print(mayor_cantidad)


dinero()
                 

            
        
    