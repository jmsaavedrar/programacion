#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
from matplotlib import pyplot


def menu():
    print("*********************************************")
    print("*******        CRYPTO MARKET             ****")
    print("*********************************************")
    print(" 1. Gráfico de valorización")
    print(" 2. Gráfico de días al alza y días a la baja")
    print(" 3. Salir")    
    print("*********************************************")
    opcion = int(input("[opcion]>"))
    return opcion
    
opcion = menu()

""" Descomentar para utilizar:
while opcion != 3:
    if opcion == 1:
        pass
    elif opcion == 2:
        pass

    opcion = menu()
"""
