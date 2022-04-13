#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 11:12:44 2022

@author: jsaavedr
Ejercicio 11, ordenamiento de números aleatorios
"""
import random

n_datos = int(input('Ingrese cantidad de datos :'))

datos = []

for i in range(n_datos):
    datos.append(random.randint(0, 100))

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
