import subprocess

class limpiar_caché_DNS:
    def __init__(self):
        pass

    def limpiar(self):
        try:
            self.limpiar_caché = subprocess.run(["ipconfig", "/flushdns"], capture_output=True, text=True) # obtenemos la salida stdout y stderr con capture_output=True y text=True lo convierte a string en lugar de que sean solo a bytes
            if self.limpiar_caché.returncode == 0:
                print("se ha limpiado la caché correctamente")
                

                with open ("caché.log", "a") as log_dns: # a sirve para crear el archivo
                    log_dns.write(self.limpiar_caché.stdout) # cojer la salida stdout que es la salida normal que nos dá la terminal del comando 
                    log_dns.write("\n")
                    print("se ha creado el log")

                return True
                
                
            else:
                print("No se ha podido limpiar la caché correctamente")
                return False

    

        except PermissionError as P:
            print(f"no se ha podido limpiar la caché correctamente:{P}")
        except OSError as O:
            print(f"Error del sistema operativo:{O}")
            return O
        except Exception as E:
            print(f"Error inesperado:{E}")
            return E

    def ver_log_caché(self):
        with open("caché.log", "r") as log_dns:
            return log_dns.read() # lo leemos

if __name__ == "__main__":
    l = limpiar_caché_DNS() # El constructor necesita un argumento obligatoriamente porque yo lo he decidido así
    l.limpiar()
