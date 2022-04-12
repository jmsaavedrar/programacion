"""
Union de listas ordenadas
"""

A = [1, 5, 10, 13, 13, 20]
B = [2, 3, 8, 17, 19, 22,30,50]
#C= [1,2,3,5,8,10,13,13,17,19,20, 22, 30, 50]

i = 0
j = 0
nA = len(A)
nB = len(B)
C = []
while i < nA and j < nB:
    if A[i] <= B[j] :        
        C.append(A[i])
        i = i + 1
    else :
        C.append(B[j])
        j = j + 1
    
while i < nA :
    C.append(A[i])
    i = i + 1

while j < nB :
    C.append(B[j])
    j = j + 1

print(C)
            
    



