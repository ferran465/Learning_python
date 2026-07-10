import sys

x = 10**100

y = 199**899 

def numeros(): 
    if x >= y: 
        print(sys.getsizeof(x))
    else:
        print(sys.getsizeof(y)) 
      
numeros()


