#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 11:28:07 2022

@author: jsaavedr
"""
import random

n_datos = int(input('Ingrese cantidad de datos:'))

datos = []
for _ in range(n_datos):
    datos.append(random.random()*6 + 1)

histograma = [0,0,0,0,0,0]

for i in range(n_datos) :
    dato = datos[i]
    if dato == 7 :
        pos = 5;
    else   :
        pos = int(dato) - 1 
    print(pos)
    histograma[pos] = histograma[pos] + 1
    
print(datos)
print(histograma)
                    