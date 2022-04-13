#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 17:31:43 2022

@author: jsaavedr
"""

import random

n_datos = int(input('Ingrese cantidad de datos:'))

datos = []
for _ in range(n_datos):
    datos.append(random.randint(0, 9))

histograma = [0,0,0,0,0,0,0,0,0,0]

for i in range(n_datos) :    
    histograma[datos[i]] = histograma[datos[i]] + 1
    
for i in range(len(histograma)):
    print('{} -> {}'.format(i, '*'*histograma[i]))
    
#print(datos)
#print(histograma)