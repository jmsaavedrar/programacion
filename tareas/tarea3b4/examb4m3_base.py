"""
Programación
Examnen bloque4 módulo 4
"""
import catalog
import numpy as np


def reportar(data):
    for item in data :
        print(item)
        
def obtener_total_por_vendedor(data):
    dict = {}

    return dict


def obtener_total_marca_por_vendedor(data):
    dict = {}
    
    return dict


def obtener_vendedor_max_dscto(data):
    dict = {}
    
    return dict

def obtener_precio_promedio_vendedor(data):
    dict = {}
    
    return dict


def obtener_marcas_vendedores(data):
    dict = {}
    
    return dict

def buscar(data, descripcion):       
    posiciones = []
    
    return posiciones


if __name__ == '__main__' :
    data = catalog.read_catalog()
    """
    puede descomentar las siguientes llamadas para ver los resultados
    """    
    reportar(data)
    #Ejercicio 1
    print(obtener_total_por_vendedor(data))
    #Ejercicio 2
#    print(obtener_total_marca_por_vendedor(data))
    #Ejercicio 3
    #print(obtener_vendedor_max_dscto(data))
    #Ejercicio 4
    #print(obtener_precio_promedio_vendedor(data))
    #Ejercicio 5
    #print(obtener_marcas_vendedores(data))    
    #Ejercicio 6
    #print(buscar(data, 'Alexa voice control'))
    
