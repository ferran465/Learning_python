import keyboard
import subprocess
import os
while True:
    if keyboard.is_pressed("esc") == True:

        os.chdir(os.path.expanduser("~/Downloads")) # os.path.expanduser se usa para utilizar una ruta más inicial para el usuario des de home y utlizar-la como base para cualquier otra ruta
                                                    # lo que hace es traducir ~ porque os.chdir no lo entiende y lo traduce literal entonces con .expanduser lo que hace es traducirle a os.chdir esa ruta. 
        subprocess.run("type nul > hola.txt", shell= True)