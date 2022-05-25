"""
Un simple gráfico de barras
que muestra el promedio de notas en cada módulo
"""

import numpy as np
import matplotlib.pyplot as plt

promedios = [5.6, 6.2, 5.0, 6.8]
modulos = ['M1', 'M2', 'M3', 'M4']
plt.bar(modulos, promedios)
plt.show()