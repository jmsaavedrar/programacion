#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from numpy import random
import biblioteca as bb
"""
Formato de la biblioteca de musica:
    
biblioteca = {
        'generos' : [],    # lista de strings con generos musicales
        'artistas' : {},   # diccionario con informacion de artistas
        'discos' : [],     # lista de diccionarios con info de discos
        'canciones' : []   # lista de diccionarios con info de canciones
    } 
"""

def crear_biblioteca_vacia():
    biblioteca = {
            'generos' : [],
            'artistas' : {},
            'discos' : [],
            'canciones' : []
        }
    return biblioteca

def buscar_genero(lista, val):
    pos = -1
    i = 0
    while pos == -1 and i < len(lista) :
        if lista[i] == val :
            pos = i
        i = i + 1
    return i
    
def crear_artista(nombre, genero, biblioteca):
    ans = False
    if not nombre in biblioteca['artistas'] :
        generos = biblioteca['generos']
        if not genero in generos :
             biblioteca['generos'].append(genero)
        id = find_genero(generos, genero)
        artista = {'nombre' : nombre, 'idx_genero':id, 'idx_discos': []}
        biblioteca['artistas'][nombre] = artista
    return ans

def crear_disco(nombre, fecha, artista, biblioteca):
    disco = {'nombre': nombre, 'fecha': fecha, 'idx_canciones': []}
    biblioteca['discos'].append(disco)
    biblioteca['artistas'][artista]['idx_discos'].append(len(biblioteca['discos']) - 1)
    return len(biblioteca['discos']) - 1 

def mostrar_disco(idx_disco, biblioteca):
    pass # borrar 'pass' y escribir aquí código de la función.

def buscar_idx_disco_por_idx_cancion(idx_cancion, biblioteca):
    return None

def buscar_por_subpalabra(subpalabra, biblioteca):
    resultados = { 'artistas' : [],
                   'idx_discos' : [], 
                   'idx_canciones' : [] }
    return resultados
    
def buscar_artistas_por_genero(genero, biblioteca):
    return []

def obtener_lista_aleatoria_reproduccion_por_genero(genero, tiempo_min, biblioteca):
    return []


###### No modificar las siguientes funciones ######

def tiempo_a_segundos(hhmmss):
    campos = hhmmss.split(":")
    return int(campos[2])+int(campos[1])*60+int(campos[0])*60*60

def obtener_idxs_discos_de_artista(artista, biblioteca):
    idx_discos = biblioteca['artistas'][artista]['idx_discos'][:]
    return idx_discos

def crear_cancion(titulo, duracion, idx_disco, biblioteca):
    cancion = { 'titulo' : titulo,
                'duracion' : duracion }
    biblioteca['canciones'].append(cancion)
    idx_cancion = len(biblioteca['canciones']) - 1
    biblioteca['discos'][idx_disco]['idx_canciones'].append(idx_cancion)
    return idx_cancion

def tui_crear_artista(biblioteca):
    nombre, genero = '', ''
    while len(nombre) == 0:
        nombre = input("[nombre]>")
    while len(genero) == 0:
        genero = input("[genero]>")
    crear_artista(nombre, genero, biblioteca)
    
def tui_crear_disco(biblioteca):
    nombre, fecha, artista = '', '', ''
    while len(nombre) == 0:
        nombre = input("[nombre]>")
    while len(fecha) == 0:
        fecha = input("[fecha (dd/mm/aaaa)]>")
    artista_existe = False
    while len(artista) == 0 or not artista_existe:
        artista = input("[artista]>")
        if artista in biblioteca['artistas']:
            artista_existe = True
            
    idx_disco = crear_disco(nombre, fecha, artista, biblioteca)
    
    linea = input("[titulo] [hh:mm:ss]>")
    while len(linea) > 0:
        datos_cancion = linea.split()
        duracion = datos_cancion[-1]
        titulo = ' '.join(datos_cancion[:-1])
        crear_cancion(titulo, duracion, idx_disco, biblioteca)
        linea = input("[titulo] [hh:mm:ss]>")
        
def tui_buscar(biblioteca):
    palabra_busqueda = ''
    while len(palabra_busqueda) == 0:
        palabra_busqueda = input("[buscar]>")
    resultados = buscar_por_subpalabra(palabra_busqueda, biblioteca)
    print("Resultados de busqueda:")
    print("Artistas:")
    for artista in resultados['artistas']:
        print(f"- {artista}")
    print("Discos:")
    for idx_disco in resultados['idx_discos']:
        print(f"- {biblioteca['discos'][idx_disco]['nombre']}")    
    print("Canciones:")
    for idx_cancion in resultados['idx_canciones']:
        print(f"- {biblioteca['canciones'][idx_cancion]['titulo']}")
    
def tui_ver_discos_de_artista(biblioteca):
    artista = ""    
    while len(artista) == 0:
        artista = input("[nombre_artista]> ")
        idx_discos = obtener_idxs_discos_de_artista(artista, biblioteca)
        for idx in idx_discos:
            mostrar_disco(idx, biblioteca)
                
def tui_ver_generos(biblioteca):
    for genero in biblioteca['generos']:
        print(f"- {genero}")
        
def tui_ver_artistas_por_genero(biblioteca):
    genero = ''
    while len(genero) == 0:
        genero = input("[genero]> ")
    artistas = buscar_artistas_por_genero(genero, biblioteca)
    for artista in artistas:
        print(f"- {artista}")
        
def tui_crear_lista_aleatoria_por_genero(biblioteca):
    genero = ''
    while len(genero) == 0:
        genero = input("[genero]> ")
    tiempo = ''    
    while len(tiempo) == 0:
        tiempo = input("[hh:mm:ss]> ")
    tiempo_s = tiempo_a_segundos(tiempo)

    lista = obtener_lista_aleatoria_reproduccion_por_genero(genero,\
                                                            tiempo_s,\
                                                            biblioteca)
    for i, idx in enumerate(lista):
        datos_disco = buscar_idx_disco_por_idx_cancion(idx, biblioteca)
        
        cancion = biblioteca['canciones'][idx]
        print(f"{i+1}. {datos_disco[1]['nombre']} / {cancion['titulo']} / {cancion['duracion']}")
        
def mostrar_menu():
    while True:
        print("-------------------------------------------")
        print("-- 𝄞 WANDES MUSIC 𝄢                      --")
        print("-------------------------------------------")
        print("- 1. Crear artista")
        print("- 2. Crear disco")
        print("- 3. Buscar")
        print("- 4. Ver discos de artista")
        print("- 5. Ver generos")
        print("- 6. Ver artistas por genero")
        print("- 7. Crear playlist aleatorio por genero")
        print("- 8. Salir")
        print("-------------------------------------------")
        opcion = int(input("> "))
        while opcion not in range(1,9):
            opcion = int(input("[1-8]> "))
            
        if opcion == 1:
            tui_crear_artista(bb.biblioteca)
        elif opcion == 2:
            tui_crear_disco(bb.biblioteca)
        elif opcion == 3:
            tui_buscar(bb.biblioteca)
        elif opcion == 4:
            tui_ver_discos_de_artista(bb.biblioteca)
        elif opcion == 5:
            tui_ver_generos(bb.biblioteca)
        elif opcion == 6:
            tui_ver_artistas_por_genero(bb.biblioteca)
        elif opcion == 7:
            tui_crear_lista_aleatoria_por_genero(bb.biblioteca)
        if (opcion == 8):
            break

# Comentar esta linea para dejar de iniciar el programa con el menu:
#mostrar_menu()
crear_artista('Jose Saavedra', 'Pop', bb.biblioteca)
artistas = bb.biblioteca['artistas']
for key in artistas :
    print(artistas[key])

# for genero in bb.biblioteca['generos']:
    # print(genero)
    #
# id = crear_disco('xxx', '17/05/2022', 'Jose Saavedra', bb.biblioteca)
#
# for i,disco in enumerate(bb.biblioteca['discos']) :
    # print('{} {}'.format(i, disco))
# print(bb.biblioteca['artistas']['Jose Saavedra'])
# print(id)