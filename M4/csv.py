"""
"""
f = open('lista_estudiantes.txt')
for linea in f :
    datos = linea.split(',')
    print('nombre: {}'.format(datos[0]))
    print('edad: {}'.format(datos[1]))
    print('carrera: {}'.format(datos[2]))
f.close()
    