"""
Ejemplos sobre listas
"""

import random

def f(A):
    B = [1,2,3]
    A.clear()
    for item in B:
        A.append(item)
         

if __name__ == '__main__' :
    A = [6, 3, 2, 5, 9, 7]
    print(A)
    f(A)
    print(A)
    
 
 
