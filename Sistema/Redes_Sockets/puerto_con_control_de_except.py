import socket
import os 

def scan_puertos_with_except():
    ip = str(input("Introduce una ip: "))
    puertos = [21, 22, 23, 25, 80, 443, 3306, 8080]
    for i in puertos:
        s = socket.socket()
        s.settimeout(0.1)
        try: 
            s.connect((ip, i))
            print("has been succesfull", i)

        except OSError as e:
            print(e, ip)

scan_puertos_with_except()
        