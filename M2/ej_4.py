"""
Ejercicio 4
"""

numero = int(input('Ingrese un número: '))
aux = numero
invertido = 0
cont = 0
while aux > 0 :
    r = aux % 10
    invertido = invertido*10 + r    
    aux = aux // 10
    cont = cont + 1
print('El numero invertido de ', numero, ' es ', invertido)
