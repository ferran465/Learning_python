calle = int(input("Cual es tu calle: "))

num_calle = int(input("Cual es el num de tu calle: "))

no_calle = str("No es tu calle")

si_calle = str("si es tu calle")


def calles():
    if calle == 18:
        if num_calle <= 18:
            print(si_calle)
        else:
            if calle >= 18: 
                print(no_calle)

    else:
        if calle == 36: 
            if num_calle <= 36:
                print(si_calle)

            else:
                if calle >= 36: 
                    print(no_calle)

        else:
            if calle == 64: 
                if num_calle >= 64:
                    print(si_calle)
                
                else:
                    if calle <= 64: 
                        print(no_calle)
calles()






        
    

  
    
