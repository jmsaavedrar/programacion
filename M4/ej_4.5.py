"""
"""
import matplotlib.pyplot as plt
import numpy as np

def  calcularhistograma(matriz):
    h= np.zeros(100)
    for i in range(matriz.shape[0]) :
        for j in range(matriz.shape[0]) :
            h[matriz[i][j]] += 1
    return h
        
x = np.linspace(-10,10,100)
Y = x*x

f, xs = plt.subplots(1,2)
matriz = np.random.randint(0,100, (100,100))
h = calcularhistograma(matriz)
xs[1].bar(np.arange(100), h)
plt.show()