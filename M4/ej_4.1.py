"""
Ejemplos con matrices
"""
import numpy as np

def sumar_por_filas(matriz):
    sumas = np.zeros(matriz.shape[0], dtype = np.int64)
    for i in range(matriz.shape[0]):
        suma = 0
        for j in range(matriz.shape[1]):
            suma = suma + matriz[i][j]
        sumas[i] = suma
        
    return sumas
    

def sumar_por_columnas(matriz):
    sumas = np.zeros(matriz.shape[1], dtype = np.int64)
    for j in range(matriz.shape[1]):
        suma = 0
        for i in range(matriz.shape[0]):
            suma = suma + matriz[i][j]
        sumas[j] = suma
        
    return sumas


def obtener_diagonal(matriz):
    diagonal = np.zeros(matriz.shape[0])
    for k in range(matriz.shape[0]) :
        diagonal[k] = matriz [k][k]
    return diagonal
        
matriz = np.array([[10,20,30], 
                   [20, 40, 60],
                   [40, 80, 100]], dtype = np.int32)

resultado = sumar_por_columnas(matriz)
diagonal = obtener_diagonal(matriz)
print(diagonal)
