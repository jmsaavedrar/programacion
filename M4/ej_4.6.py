"""
Usando plots para graficar funciones
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.01,10,100)

y_sqrt= np.sqrt(x)
y_log = np.log2(x)
#

plt.plot(x,y_sqrt)
plt.plot(x,y_log)
plt.title('Funciones')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend(['Raíz Cuadrada','Log'])
plt.show()
