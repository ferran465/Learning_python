import os
import subprocess
import sys
import time
import asyncio


def iniciar_server():
    try:
        # /home/ferranitoxx/Escritorio/Server-Minecraft/Paper-1.20.1
        os.chdir("/home/ferranitoxx/Escritorio/Server-Minecraft/Paper-1.20.1")

        comand = 'tmux new-session -d -s minecraft "java -Xms2G -Xmx4G -jar /home/ferranitoxx/Escritorio/Server-Minecraft/Paper-1.20.1/paper.jar nogui"' # necesitamos una terminal para tener el control de todo ya que al ejecutarlo como un subprocesso no podemos ver la interfaz gráfica de la terminal.
        X_comand = subprocess.run(comand, shell = True) # shell = True hace que pueda ejecutar el comando en un interperete de comandos como bash, bin, zsh etc...

        if X_comand.returncode == 0:
            return 0
        elif X_comand.returncode != 0:
            return 1
                

    except OSError as E:
        print(f"Ha ocurrido un error inesperado al intentar iniciar el servidor de Minecraft{E}")
        return 1 # damos una salida de error por si falla ya que 0 seria exito




result = sys.exit(iniciar_server()) # con sys.exit hace que el programa termine y que el código de salida que da iniciar_server() que antes solamente daba True ahora lo devuelva con un número

 # cuando minecraft cierra el proceso simplemente devuleve el resultado a systemd que es el que se encarga en "LINUX" de poder controlar los procesoso y los servicios

if result == 0:
    await asyncio.sleep(72000)
elif not time.sleep(5):
                                                                          # asyncio no toca el programa solo es como una sala de espera y time.sleep lo para entero hasta el tiempo que tu digas para que cuando acable lo vuelva a ejecutar
    