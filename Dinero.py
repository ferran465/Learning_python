dinero1 = float (input("Introduce una cifra de dinero: "))

menor_cantidad = "Solo puede introducir 5 o igual"

mayor_cantidad = "Tiene que introducir más dinero"

cantidad_normal = "su cantidad és exacta"

def dinero():
    if dinero1 >5:
        print(menor_cantidad)
    else:
        if dinero1 >=5:
                print(cantidad_normal)

        elif dinero1 == (0, 1, 2, 3, 4):
                print(mayor_cantidad)


dinero()
                 

            
        
    