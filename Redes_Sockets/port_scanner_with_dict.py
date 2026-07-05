import socket
import os


def ports_with_dict():

    puertos = {
        22:"ssh",
        21:"ftp",
        23: "telnet" , 
        80:"http", 
        445: "https", 
        3306: "mysql", 
    }
    ip = str(input("Itroduce una ip: "))
    for p in puertos: 
        l = socket.socket()
        l.settimeout(0.1)

        try: 
            l.connect((ip, p))
            print("has been connected", p)
            

        except OSError as e:
            print("System Error", e)

        except ValueError as s: 
            print("No es una ip válida") 
            return s
        
        # Este except probablemente nunca se ejecute con el código actual.
        # connect() delega la validación de la IP al sistema operativo,
        # que lanza OSError (no ValueError) si la IP no es válida.
        # ValueError solo saltaría si YO mismo validara el formato de la IP
        # antes de conectar (ej: separando por puntos y usando int() en cada parte).

        finally: 
            l.close()


ports_with_dict()

