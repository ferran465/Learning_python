import socket

def scan(): 
    ip = str (input("Introduce una ip valida: "))
    for i in range(1, 65536):
        s = socket.socket()
        s.settimeout(0.1)

        try: 
            s.connect((ip, i))
            print("connection succesfull", i)


        except:
            print("connection failed", i)

scan()







   
        

