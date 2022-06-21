"""
multiplicacion de matrices
"""
import numpy as np
def multiplicar_matrices(A,B):
    nfilas_A = A.shape[0] 
    nfilas_B = B.shape[0]
    ncols_A = A.shape[1]
    ncols_B = B.shape[1]
    C = np.zeros((nfilas_A, ncols_B))
    for i in range(nfilas_A) :
        for j in range(ncols_B) :
            #sacar fila de A
            #A[i,:]
            #sacar col de B
            #B[:,j]            
            C[i][j] = np.sum(A[i,:]*B[:,j])          
    return C

A = np.array([[1,2,3], [4,5,6], [7,8,9]])
B = np.array([[2,4], [6,8], [10,12]])

print(A.shape)
print(B.shape)
if A.shape[1] == B.shape[0] :
    print('OK')
    #versiín propia
    print('AxB versión propia')
    C = multiplicar_matrices(A, B)
    #versión numpy
    print('AxB versión numpy')
    C1 = np.matmul(A,B)
    print(C)
    print(C1)
else :
    print('no se pueden multiplicar') 
