"""
return position if the val exists or -1 if not
"""

A = [2, 4, 17, 34, 37, 49, 69, 71, 90, 94]


def b_search(A, valor, i, j):
    if i<=j :
        k = (i+j) // 2
        if valor==A[k] :
            return k
        elif valor < A[k] :
            return b_search(A, valor, i,k-1)
        else :
            return b_search(A, valor, k+1,j)
    else :
        return -1
        
    

pos = b_search(A, 71, 0, len(A)-1)
print(pos)
if pos >= 0 :
    print(A[pos])
        
        