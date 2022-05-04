"""
"""

import random

def generar_random():    
    return random.randint(0,10)



def imprimir_mensaje(mi_mensaje):
    print('Mensaje: {} '.format(mi_mensaje))


#a = generar_random()
#print(a)
imprimir_mensaje('Hola esto es una prueba')
