#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 11 09:24:07 2022

@author: jsaavedr
"""
def reportar(lista) :
    for item in lista :
        print('nombre: {} edad: {} carrera: {}'.format(item['nombre'], item['edad'], item['carrera']))

def reportar_por_posiciones(lista, posiciones) :
    print('Resultado')
    for pos in posiciones :
        item = lista[pos]
        print('nombre: {} edad: {} carrera: {}'.format(item['nombre'], item['edad'], item['carrera']))    

def buscar_por_carrera(lista, una_carrera) :
    posiciones = []
    for pos, item in enumerate(lista) :
        if item['carrera'] == una_carrera :
            posiciones.append(pos)
    return posiciones

def buscar_por_nombre(lista, un_nombre) :
    posiciones = []
    for pos, item in enumerate(lista) :
        if item['nombre'] == un_nombre :
            posiciones.append(pos)
    return posiciones

lista_estudiantes = [{'nombre':'Juan', 'edad': 20, 'carrera': 'Industrial'},
                     {'nombre':'Pedro', 'edad': 22, 'carrera': 'Computación'},
                     {'nombre':'Ana', 'edad': 21, 'carrera': 'Industrial'},
                     {'nombre':'Camila', 'edad': 20, 'carrera': 'Computación'},
                     ]


lista_estudiantes.append({'nombre':'Violeta', 'edad': 23, 'carrera': 'Computación'})


#reportar(lista_estudiantes)
#lista_pos = buscar_por_carrera(lista_estudiantes, 'Industrial')
lista_pos = buscar_por_nombre(lista_estudiantes, 'Juan')
reportar_por_posiciones(lista_estudiantes, lista_pos)
