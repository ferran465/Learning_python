
numero = float(input("Introduce un numero: "))

def es_multiplo(multiplo, numero):
    if multiplo % numero == 0:
        return True
        
    else:
        return False
       
        
print(es_multiplo(1, numero))
print(es_multiplo(0, numero))





   
        
