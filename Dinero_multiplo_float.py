dinero1 = float(input("Introduce una cifra de dinero: "))

mayor_cantidad = "Solo puede introducir 5 o más"

cantidad_normal = "su cantidad és exacta"

cantidad_excesiva = "su cantidad no puede ser mayor a 10000"

si_multiplo = "Su numero és multiplo"

no_multiplo = "Su numero no és multiplo"

def dinero():
        if dinero1 >10000:
            print(float(dinero1), cantidad_excesiva)

        elif dinero1 >=5:
            for m in range(5, 10001):
                if dinero1 == m:
                    print(float(dinero1), cantidad_normal)

        elif dinero1 <5:
            for i in range(0, 4):
                if dinero1 == i:
                    print(float(dinero1), mayor_cantidad)

        if dinero1 % 5 == 0: 
            print(float(dinero1), si_multiplo)
        else: 
            print(float(dinero1), no_multiplo)
dinero()
                 

            
        
    