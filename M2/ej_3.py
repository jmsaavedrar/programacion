"""
Ejercicio 3
"""

numero = int(input('Ingrese un número: '))
aux = numero
cont = 0
while aux > 0 :
    aux = aux // 10
    cont = cont + 1
print('El numero ', numero, ' tiene ', cont, ' digitos')
