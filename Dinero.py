dinero1 = float (input("Introduce una cifra de dinero: "))

menor_cantidad = "Solo puede introducir 10000 o menos"

mayor_cantidad = "Tiene que introducir más dinero"

def dinero():
    if dinero1 <=5:
        for i in range(0, 5):
            print((mayor_cantidad))
            return i
    else:
        if dinero1 >5:
            print(menor_cantidad) 

dinero()
                 

            
        
    