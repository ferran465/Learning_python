import socket

ip = "192.168.1.1"

puerto = 4444

paquetes = 200000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # AF_INET para decir que tipo de dirección ip quiero es decir IPV4 y SOCK_DGRAM para poder enviar paquetes UDP paquetes inestables que no importan si llegan o no

try:
    while True:
        s.sendto(b"paquetes", (ip, puerto)) # sendto() lo que hace es enviar algo a la ip y puerto
        print(f"se ha podido enviar correctamente {paquetes} paquetes a este {ip, puerto}")


except OSError as E:
    print(f"no se ha podido conectarse con{ip, puerto}, {E}")
