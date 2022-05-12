#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 11 10:10:11 2022

@author: jsaavedr
"""
def recorrer_matriz(M):
    n_filas = len(M)
    n_columnas = len(M[0])
    
    for i in range(n_filas):
        for j in range(n_columnas) :
            if M[i][j] == 0 :
                print(' ', end = ' ')
            else:   
                print('*', end = ' ')
        print()

    
    
    
    
M = [ [0, 0, 0, 0, 0, 0],
      [0, 0, 1, 1, 0, 0], 
      [0, 1, 0, 0, 1, 0], 
      [0, 0, 1, 1, 0, 0], 
      [0, 0, 0, 0, 0, 0], 
     ]

recorrer_matriz(M)
