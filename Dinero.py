dinero1 = float (input("Introduce una cifra de dinero: "))

menor_cantidad = "Solo puede introducir 5 o más"

mayor_cantidad = "Tiene que introducir más dinero"

cantidad_normal = "su cantidad és exacta"

def dinero():
    if dinero1 >5:
        for i in range(0, 5):
            print((menor_cantidad))
            if dinero1 >5:
                print(cantidad_normal)
                return i
    else:
        if dinero1 <5:
            for i in range(0, 5):
                print(mayor_cantidad)
                return i 


dinero()
                 

            
        
    