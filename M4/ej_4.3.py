"""
Un simple ejemplo para resolver sistemas de ecuaciones lineales
6x + 2y = 11
8x + 3y = 16

Cuánto valen x e y?

Al ejecutar este script tendrás las respuestas en X

"""
import numpy as np

A =  np.array([[6,2], [8,3]], dtype = np.float32)
b =  np.array([11,16], dtype = np.float32)

X = np.linalg.solve(A,b)
print(X)

