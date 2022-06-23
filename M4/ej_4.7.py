"""
Un simple gráfico de barras
que muestra el promedio de notas en cada módulo
"""

import numpy as np
import matplotlib.pyplot as plt

promediosA = [5.6, 6.2, 5.0, 6.8]
promediosB = [7.0, 6.8, 6.0, 5.0]
modulos = ['M1', 'M2', 'M3', 'M4']
plt.plot(modulos, promediosA)
plt.plot(modulos, promediosB)
plt.title('Graficos')
plt.xlabel('Modulos')
plt.ylabel('promedio')
plt.legend(['grupo A ','grupoB'])
plt.show()