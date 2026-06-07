import socket

ip = str(input("Introduce una ip valida para conectarse al socket: "))

ip_Valida = "Esta ip és valida"

ip_Invalida = "Esta ip no és valida"

puerto_abierto = "Este puerto está abierto"

def Socket():
    for i in range(0, 65536): 
        s = socket.socket()
        s.settimeout(0.1)

        
        try: 
            s.connect((ip, i))
            print(ip_Valida)
            print(puerto_abierto, i)

        except: 
            pass


Socket()



