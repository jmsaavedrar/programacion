"""
extensión
"""

archivo = input('Ingrese nombre de archivo: ')
pos = archivo.rfind('.')
largo = len(archivo)
extension = archivo[pos+1: largo]
print('Extensión: ', extension)

