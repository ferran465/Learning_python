import sys


num1 = int(input("Introduce num1: "))
num2 = int(input("Introduce num2: "))

size1 = sys.getsizeof(num1)
size2 = sys.getsizeof(num2)



def numeros():
    if size1 >= size2:
        print(size1)
    else:
        print(size2)

numeros()


