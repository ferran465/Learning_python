import sys

numeros = str(input("Introduce una letra: "))


x = 1000000000 * 1000000000 * 1000000000

y = 2000000000 * 2000000000 * 2000000000

def numeros(): 
    if x < y: 
        print(sys.getsizeof(x))
    else:
        print(sys.getsizeof(y))

numeros()