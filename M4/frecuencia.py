"""
frecuencia de aleatorios y gráfico de barras
"""
import numpy as np
import matplotlib.pyplot as plt

#vector
#Generar un array aleatorio de n valores 
#con valores entre 0 y 100
#contar la frecuencia de aparición de
#cada valor

def contar_frecuencia(A, n_valores):
    conteo = np.zeros(n_valores)
    for val in A :
        conteo[val] += 1
    return conteo
    

n = 10000
n_valores = 100
a = np.random.randint(0,n_valores, size = n)
conteo = contar_frecuencia(a, n_valores)
print(conteo)
plt.bar(range(n_valores), conteo)
plt.show()
