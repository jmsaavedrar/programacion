"""
Ejercicio 6
"""

N = int(input('N: '))
i = 0
suma = 0
mayor = 0
menor = 0
while i < N :
    num = float(input('numero {} :'.format(i+1)))
    if i == 0 :
        mayor = num
        menor = num
    else :
        if num > mayor :
            mayor = num
        if num < menor :
            menor = num
    suma = suma + num
    i = i + 1
promedio = suma / N
print('Mayor: ', mayor)
print('Menor: ', menor)
print('Promedio: ', promedio)