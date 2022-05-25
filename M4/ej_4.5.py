"""
Calculando histogramas de una matriz generada aleatoriamente.

Dado que los valores aleatorios siguen una distribución uniforme
el gráfico de barras se observa ecualizado, es decir todos los números) tienen
similar número de aparición en la matriz.
"""
import matplotlib.pyplot as plt
import numpy as np

def  calcular_histograma(matriz):
    h= np.zeros(100)
    for i in range(matriz.shape[0]) :
        for j in range(matriz.shape[0]) :
            h[matriz[i][j]] += 1
    return h
        


matriz = np.random.randint(0,100, (100,100))
h = calcular_histograma(matriz)
plt.bar(np.arange(100), h)
#plt.hist(np.reshape(matriz, (-1,)), 10)
plt.show()

A = np.array([1,2,3,4,5])
print(A[A%2 == 0]) 




