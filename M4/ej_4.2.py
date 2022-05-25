"""
Ejemplos con matrices y funciones de numpy
"""
import numpy as np


matriz = np.array([[10,20,30], 
                   [20, 40, 60],
                   [40, 80, 100]])


#suma por filas
suma_por_filas = np.sum(matriz, axis = 1)
suma_por_columnas = np.sum(matriz, axis = 0)
diagonal = np.diag(matriz)
print('suma_por_fila={}'.format(suma_por_filas))
print('suma_por_columnas={}'.format(suma_por_columnas))
print('diagonal= {}'.format(diagonal))
