import os
import subprocess
import sys
import time
import asyncio
import keyboard

def iniciar_server():
    try:
        # /home/ferranitoxx/Escritorio/Server-Minecraft/Paper-1.20.1
        os.chdir("/home/ferranitoxx/Escritorio/Server-Minecraft/Paper-1.20.1")

        comand = 'tmux kill-session -t minecraft; tmux new-session -d -s minecraft "java -Xms2G -Xmx4G -jar /home/ferranitoxx/Escritorio/Server-Minecraft/Paper-1.20.1/paper.jar nogui"' # necesitamos una terminal para tener el control de todo ya que al ejecutarlo como un subprocesso no podemos ver la interfaz gráfica de la terminal.
        X_comand = subprocess.run(comand, shell = True) # shell = True hace que pueda ejecutar el comando en un interperete de comandos como bash, bin, zsh etc...

        if X_comand.returncode == 0:
            return 0
        elif X_comand.returncode != 0:
            return 1
                

    except OSError as E:
        print(f"Ha ocurrido un error inesperado al intentar iniciar el servidor de Minecraft{E}")
        return 1 # damos una salida de error por si falla ya que 0 seria exito


async def reiniciar_server(): # con async lo que hace es que la parte del programa o bloque del programa que hayas definido junto async se congele durante un tiempo para que después pueda ejecutarse cuando le toque. 
    try:
        while True: # es mejor no poner returns dentro de el bucle ya que los returns acaban con el programa o se salen del programa
            result = iniciar_server()

            if result == 0:
                await asyncio.sleep(72000)
                time.sleep(60)
            elif result != 0:
                print("no se ha podido reiniciar correctamente")
                time.sleep(60)
    except OSError as error_inesperado:
        print(f"ha habido un error inesperado{error_inesperado}")
        if error_inesperado == True:
            pass
        if not error_inesperado == True:
            os.chdir("/home/ferranitoxx/Escritorio/Server-Minecraft/Información_del_server/Logs_de_reinicio_tmux")
            with open("log.txt", "a") as errn:
                errn.write(f"{error_inesperado}")

            with open("log.txt", "r") as errn:
                errn.read()

        else:
            pass

def apagar_maquina(): # otra cosa está función no se llama normal como haria con reiniciar_server() o iniciar_server() abajo del código hay una función que activa la funcíón que activa está misma función en cuanto presionas las teclas "alt + shift + *" 
    try:
        subprocess.run("sudo shutdown now", shell=True)
    except OSError as hotkey_start_errn:
        print(f"no se ha podido encontrar la tecla{hotkey_start_errn}")
        os.chdir("/home/ferranitoxx/Escritorio/Server-Minecraft/Información_del_server/Logs_de_apagado")
        with open("log_de_apagado.txt", "a") as shutdowning_log:
            shutdowning_log.write(f"{hotkey_start_errn}")

        with open("log_de_apagado.txt", "r") as shutdowning_log:
            shutdowning_log.read()

keyboard.add_hotkey("alt + shift + f12", apagar_maquina) # con f12
# no puede ir dentrro del try porque basicamente si se pusiera dentro se retroalimentaria como si fuera un bucle llamando una y otra vez para que pulses el hotkey 

def reiniciar_maquina():
    try:
        subprocess.run("sudo reboot -f", shell=True)
    except OSError as hotkey_reboot_errn:
        print(f"no se ha podido encontrar la tecla{hotkey_reboot_errn}")
        os.chdir("/home/ferranitoxx/Escritorio/Server-Minecraft/Información_del_server/Logs_de_reinicio")
        with open("log_de_reinicio.txt", "a") as reset_log:
            reset_log.write(f"{hotkey_reboot_errn}")

        with open("log_de_reinicio.txt", "r") as reset_log:
            reset_log.read()

keyboard.add_hotkey("alt + shift + f9", reiniciar_maquina) # con f9

def suspender_maquina():
    try:
        subprocess.run("pm-suspend", shell=True)
        subprocess.wait()
    except OSError as hotkey_suspend_errn:
        print(f"no se ha podido suspender la máquina{hotkey_suspend_errn}")
        os.chdir("/home/ferranitoxx/Escritorio/Server-Minecraft/Información_del_server/Logs_de_suspendido")
        with open("log_de_suspendido.txt", "a") as suspend_log:
            suspend_log.write(f"{hotkey_suspend_errn}")
            
        with open("log_de_suspendido.txt", "r") as suspend_log:
            suspend_log.read()
            
keyboard.add_hotkey("alt + shift + f8", suspender_maquina) # con f8

asyncio.run(reiniciar_server()) # asyncio.run sirve para ejecutar la función asincronico definida
sys.exit(iniciar_server()) # con sys.exit hace que el programa termine y que el código de salida que da iniciar_server() que antes solamente daba True ahora lo devuelva con un número

 # cuando minecraft cierra el proceso simplemente devuleve el resultado a systemd que es el que se encarga en "LINUX" de poder controlar los procesoso y los servicios
                                                    # asyncio no toca el programa solo es como una sala de espera y time.sleep lo para entero hasta el tiempo que tu digas para que cuando acable lo vuelva a ejecutar