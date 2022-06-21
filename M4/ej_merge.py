"""
merge dos listar ordenadas
"""

def merge(A, B):
    nA = len(A)
    nB = len(B)
    i = 0
    j = 0
    result = []
    while i< nA and j < nB :
        if A[i] <= B[j] :
            result.append(A[i])
            i +=1 
        else :
            result.append(B[j])
            j +=1
    while i < nA :
        result.append(A[i])
        i +=1
    
    while j < nB :
        result.append(A[j])
        j +=1
    return result


A = [3,7,11,20]
B = [1,2,8]
C = merge(A,B)
print(C)
        
        