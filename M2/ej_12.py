#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 11:12:44 2022

@author: jsaavedr
Ejercicio 12, ordebamiento de números aleatorios
"""
import random

n_datos = int(input('Ingrese cantidad de datos :'))

datos = []

for _ in range(n_datos):
    datos.append(random.randint(0, 10))

print(datos)
for i in range(n_datos - 1):
    mayor = datos[i]
    pos = i
    for j in range(i+1, n_datos):
        if datos[j] > mayor:
            mayor = datos[j]
            pos = j
    datos[pos] = datos[i]
    datos[i] = mayor
        
print(datos)


#eliminar repetidos
datos_sin_repetidos = []
i = 0
while i < n_datos :
    dato = datos[i] 
    datos_sin_repetidos.append(dato)
    i = i + 1
    while i < n_datos and  dato == datos[i] : 
        i = i + 1
        
print(datos_sin_repetidos)
        
    
    

