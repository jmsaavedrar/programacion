"""
return position if the val exists or -1 if not
"""




def b_search(A, valor, i, j):
    pos = -1
    if i<=j :
        k = (i+j) // 2
        if valor==A[k] :
            return k
        elif valor < A[k] :
            pos = b_search(A, valor, i,k-1)
        else :
            pos = b_search(A, valor, k+1,j)

    return pos    
    

A = [2, 4, 17, 34, 37, 49, 69, 71, 90, 94]



pos = b_search(A, 10, 0, len(A)-1) 
print(pos)
if pos >= 0 :
    print('val: {}'.format(A[pos]))
        
        