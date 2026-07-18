import os
import platform

class shutdown_os:
    def __init__(self):
        pass
    def S_Windows(self):
        try:
            self.Windows = os.system("shutdown/s /t 1")   # un atributo es una variable que sirve para guardarlo y cuando lo necesites ussarlo en otros métodos
            if self.Windows == 0: # Si la salida es 0 es porque se ha podido ejecutar, si no es 0 es porque ha habido un error
                return True
            else: 
                return False
        except OSError as w:
            print("Tu sistema no se ha podido apagar correctamente")
            return w

    def S_Linux(self):
        try: 
            self.Linux = os.system("sudo shutdown -h 0")
            if self.Linux == 0:
                return True
            else:
                return False 
        except OSError as l:
            print("Tu sistema no se ha podido apagar correctamente")
            return l
    def S_MacOS(self):
        try:
            self.MacOS = os.system("sudo shutdown -h now")
            if self.MacOS == 0:
                True
            else: 
                return False
        except OSError as m:
            print("Tu sistema no se ha podido apagar correctamente")
            return m
if __name__ == "__main__":
    s = shutdown_os()
    system = platform.system()
    if system == "Windows":
        s.S_Windows()
    elif system == "Linux":
        s.S_Linux()
    elif system == "Darwin":
        s.S_MacOS()

        


    

