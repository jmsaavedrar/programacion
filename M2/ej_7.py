"""
Ejercicio 6
"""

i = 0
suma = 0
mayor = 0
menor = 0
num = float(input('numero: '))
while num != -111:
    if i == 0 :
        mayor = num
        menor = num
    else :
        if num > mayor :
            mayor = num
        if num < menor :
            mnenor = num
    suma = suma + num
    i = i + 1
    num = float(input('numero: '))
promedio = suma / i
print('Cantidad: ', i)
print('Mayor: ', mayor)
print('Menor: ', menor)
print('Promedio: ', promedio)