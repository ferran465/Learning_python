import os
import subprocess

def iniciar_server():
    try:
        # /home/ferranitoxx/Escritorio/Server-Minecraft/Paper-1.20.1
        os.chdir("/home/ferranitoxx/Escritorio/Server-Minecraft/Paper-1.20.1")

        comand = 'java -Xms2G -Xmx4G -jar /home/ferranitoxx/Escritorio/Server-Minecraft/Paper-1.20.1/paper-1.20.1.jar --nogui' 
        X_comand = subprocess.run(comand, shell = True) # shell = True hace que pueda ejecutar el comando en un interperete de comandos como bash, bin, zsh etc...

        if X_comand.returncode == 0:
            return True
        elif X_comand.returncode != 0:
            return False
                

    except OSError as E:
        print("Ha ocurrido un error inesperado al intentar iniciar el servidor de Minecraft")
        return E

    
iniciar_server()