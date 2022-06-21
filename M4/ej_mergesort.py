"""
MergeSort
"""

def mergesort(lista, i, j):
    """
    mergesort recursivo
    """
    if i<j :
        k = (i + j) // 2
        mergesort(lista, i, k)
        mergesort(lista, k+1, j)
        merge(lista, i, k, j)


def merge(lista, i, k, j):
    """
    mezcla dos listas lista[i..k] lista[k+1...j]
    """
    lista_1 = []
    p1 = i
    p2 = k+1
    while p1 <= k and p2 <= j :
        print('{} {} {}'.format(p1,p2, lista))
        if lista[p1] < lista[p2] :
            lista_1.append(lista[p1])
            p1 += 1
        else :
            lista_1.append(lista[p2])
            p2 += 1
            
    while p1 <= k :
        lista_1.append(lista[p1])
        p1 += 1
        
    while p2 <= j :
        lista_1.append(lista[p2])
        p2 += 1
                
    lista[i:j+1]=lista_1

import  numpy as np
A =[]

for i in range(10) :
    A.append(np.random.randint(0,100))
    
mergesort(A, 0, len(A)-1)
print(A)



