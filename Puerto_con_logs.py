import socket

ip = str(input("Introduce una ip valida: " ))

puerto_no_conectado = "Failed"

puerto_conectado = "Conected"

lista = []

def scan():
    for i in range(0, 65536):
        m = socket.socket()
        m.settimeout(0.1)

        try: 
            m.connect((ip, i))
            print(puerto_conectado, i)
            lista.append(i)
            print(lista)


        except: 
            print(puerto_no_conectado, i)

      
scan()






