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
    for item in data :
        if not item['vendedor'] in dict :
            dict[item['vendedor']] = 1
        else :
            dict[item['vendedor']] += 1
    return dict


def obtener_total_marca_por_vendedor(data):
    dict = {}
    for item in data :
        marca = item['marca']
        vendedor = item['vendedor'] 
        if not vendedor in dict :
            dict[vendedor] = {}
        if not marca in dict[vendedor] :
            dict[vendedor][marca] = 1
        else :
            dict[vendedor][marca] += 1                                    
    return dict


def obtener_vendedor_max_dscto(data):
    dict = {}
    for item in data :
        vendedor = item['vendedor']
        dif = item['precio_max'] - item['precio_min']
        if not vendedor in dict :
            dict[item['vendedor']] = dif
        else :
            if dif > dict[item['vendedor']] :
                dict[item['vendedor']] = dif
    return dict

def obtener_precio_promedio_vendedor(data):
    dict = {}
    for item in data :
        vendedor = item['vendedor']
        precio= item['precio_max']
        if not vendedor in dict :
            dict[item['vendedor']] = [precio]
        else :
            dict[item['vendedor']].append(precio)
            
    for vendedor in dict :
        dict[vendedor] = np.mean(np.array(dict[vendedor]))
    return dict


def obtener_marcas_vendedores(data):
    dict = {}
    for item in data :
        vendedor = item['vendedor']
        marca = item['marca']
        if not marca in dict :
            dict[marca] = []        
        if not vendedor in dict[marca] :
            dict[marca].append(vendedor)
    return dict

def buscar(data, descripcion):       
    posiciones = []
    for pos, item in enumerate(data) :
        if item['descripcion'].find(descripcion) != -1 :
            posiciones.append(pos)
    return posiciones


   
    

if __name__ == '__main__' :
    data = catalog.read_catalog()
    """
    puede descomentar las siguientes llamadas para ver los resultados
    """    
    reportar(data)
    #Ejercicio 1
    #print(obtener_total_por_vendedor(data))
    #Ejercicio 2
    #print(obtener_total_marca_por_vendedor(data))
    #Ejercicio 3
    #print(obtener_vendedor_max_dscto(data))
    #Ejercicio 4
    #print(obtener_precio_promedio_vendedor(data))
    #Ejercicio 5
    #print(obtener_marcas_vendedores(data))    
    #Ejercicio 6
    #print(buscar(data, 'Alexa voice control'))
    
