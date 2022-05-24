"""
"""
import numpy as np
matriz = np.array([[10,20, 30], [20, 40, 60]], dtype = np.float32)
array_sumas = np.zeros(matriz.shape[0], dtype=np.float32)
for i in range(matriz.shape[0]) : 
    suma = 0
    for j in range(matriz.shape[1]) :        
        suma = suma + matriz[i][j]
    array_sumas[i] = suma
print(array_sumas)

sumas = np.mean(matriz, axis = 1)
print(sumas)