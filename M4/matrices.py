"""
EJericios con numpy arrays
"""

import numpy as np

def sumar_matriz(matriz):
    nfilas = matriz.shape[0]
    ncols = matriz.shape[1]
    suma = 0;
    for i in range(nfilas) :
        for j in range(ncols) :
            suma = suma + matriz[i][j]
    return suma
def obtener_diagonal(matriz):
    nfilas = matriz.shape[0]
    ncols = matriz.shape[1]
    diagonal = np.zeros(nfilas)
    for i in range(nfilas) :
        diagonal[i] = matriz[i][i]
    return diagonal
    
    
    
    
matriz = np.array([[1,2,3], [4,5,6], [7,8,9]])
#print(matriz.shape)
#suma = sumar_matriz(matriz)
#print(suma)
#print(matriz)


diagonal = obtener_diagonal(matriz)
print(diagonal)