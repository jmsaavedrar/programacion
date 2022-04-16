"""
no digitos consecutivos
"""
entrada = input('Ingrese string: ')
estado = 0 
i = 0
N = len(entrada)

if i< N and  entrada[i].isalpha() :
    estado = 1
    i = i + 1
    
if i< N and  estado == 1 and entrada[i].isdigit() :
    estado = 2
    i = i + 1
    
while i< N and estado == 2 and entrada[i].isdigit() :
    i = i + 1
    
valido = False
if i == N and estado == 2 :
    valido = True

print(valido)    


    