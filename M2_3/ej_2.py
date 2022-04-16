"""
extensión a zip
"""

archivo = input('input: ')
pos = archivo.rfind('.')
nuevo_nombre = archivo
if pos != -1 :
    largo = len(archivo)
    extension = archivo[pos+1: largo]
    nuevo_nombre = archivo.replace(extension, 'zip')
print('output: ', nuevo_nombre)

