dinero1 = int(input("Introduce una cifra de dinero: "))

mayor_cantidad = "Solo puede introducir 5 o más"

cantidad_normal = "su cantidad és exacta"

cantidad_excesiva = "su cantidad no puede ser mayor a 10000"

def dinero():
        if dinero1 >10000:
            print(cantidad_excesiva)

        elif dinero1 >=5:
            for m in range(5, 10001):
                if dinero1 == m:
                    print(cantidad_normal)

        elif dinero1 <5:
            for i in range(0, 4):
                if dinero1 == i:
                    print(mayor_cantidad)
dinero()
                 

            
        
    