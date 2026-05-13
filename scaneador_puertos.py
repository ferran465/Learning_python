import socket


def scan(): 
    for i in range(1, 65536):
        s = socket.socket()
        s.settimeout(0.1)
        try: 
            s.connect(("172.24.99.201", i))
            print("connection succesfull", i)
            continue
            

                
                
                
        except:
            print("connection failed", i)
            continue
                    
                

print(scan())
        

