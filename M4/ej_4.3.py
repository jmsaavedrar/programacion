import numpy as np

A =  np.array([[6,2], [8,3]], dtype = np.float32)
b =  np.array([11,16], dtype = np.float32)

X = np.linalg.solve(A,b)
print(X)

