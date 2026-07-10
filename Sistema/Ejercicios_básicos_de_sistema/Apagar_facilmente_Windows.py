import os

def apagar_windows():
    try:
        os.system("shutdown/s /t 1")
    except OSError as s_w: 
        print("No se ha podido apagar el sistema correctamente")
        return s_w

apagar_windows()