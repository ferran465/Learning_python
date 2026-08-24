import subprocess

class limpiar_caché_DNS:
    def __init__(self, limpiar_caché):
        self.limpiar_caché = limpiar_caché
        

    def limpiar(self):
        try:
            self.limpiar = subprocess.run(["ipconfig", "/flushdns"], capture_output=True, text=True) # <--- se sobrescribe
            if self.limpiar.returncode == 0:
                print("se ha limpiado la caché correctamente")
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

if __name__ == "__main__":
    l = limpiar_caché_DNS("limpiar") # El constructor necesita un argumento obligatoriamente porque yo lo he decidido así
    l.limpiar()
