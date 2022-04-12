"""
Ejercicio 5
"""

palabra = input('Ingrese un string: ')

i = 0
largo  = len(palabra) 
while i <= largo - 1 - i and palabra[i] == palabra[largo - 1 - i]:
    i = i + 1
if i > largo - 1 - i :
    print('palíndroma')
else :
    print('no es palíndroma')
    