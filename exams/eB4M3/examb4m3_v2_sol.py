"""
Programación
Examnen bloque4 módulo 4
"""
import catalog
import numpy as np


def reportar(data):
    for item in data :
        print(item)
        
#Examen V2
#Ej. 1
def obtener_vendedores_y_productos(data) :
    dict = {}
    for item in data :
        vendedor = item['vendedor']
        id = item['id']
        if not vendedor in dict :
            dict[vendedor] = [id]        
        if not id in dict[vendedor] :
            dict[vendedor].append(id)
    for vendedor in dict:
        dict[vendedor] = len(dict[vendedor])
        
    return dict 
        
def ordenar(A):
    posiciones = []
    n = len(A)
    for i in range(n) :
        j = 0
        while j <  len(posiciones) and A[posiciones[j]]> A[i]:
            j += 1
        posiciones.insert(j, i)    
                            
    return posiciones
            
def obtener_mejores_vendedores(data): 
    dict = obtener_vendedores_y_productos(data)
    vendedor =  []
    cantidad = []
    for key in dict :
        vendedor.append(key)
        cantidad.append(dict[key])
    
    posiciones = ordenar(cantidad)
        
    nuevo_dict = {}
    for i, pos in enumerate(posiciones[:5]) :
        nuevo_dict[vendedor[pos]] = cantidad[pos]
    return nuevo_dict
        
def obtener_variacion_productos(data) :
    dict = {}
    for item in data:
        precio_min = item['precio_min']    
        precio_max = item['precio_max']
        id = item['id']
        if not id in dict :
            dict[id] = {'max': precio_max, 'min': precio_min}
        else :
            if precio_max > dict[id]['max'] :
                dict[id]['max'] = precio_max
            if precio_min < dict[id]['min'] :
                dict[id]['min'] = precio_min
    return  dict
    
                      
def obtener_vendedores_por_producto(data, id) :
    dict = {}
    for item in data :
        id_data = item['id']
        vendedor =  item['vendedor']
        precio_min = item ['precio_min']
        if id == id_data :
            if not vendedor in dict:
                dict[vendedor] = precio_min
            else :
                if precio_min < dict[vendedor] :
                    dict[vendedor] = precio_min
    return dict

def obtener_pos_menor(valores):
    pos = 0
    for i, val in enumerate(valores):
        if val < valores[pos] :
            pos = i
    return pos

def obtener_vendedor_mas_barato(data, id) :    
    dict = obtener_vendedores_por_producto(data, id)
    vendedor =  []
    precio = []
    for key in dict :
        vendedor.append(key)
        precio.append(dict[key])    
    pos = obtener_pos_menor(precio)
    return {'vendedor': vendedor[pos], 'precio': precio[pos]} 

def obtener_mejores_marcas(data, N) :
    dict = {}
    for item in data :
        marca = item['marca']
        vendedor = item['vendedor']
        if not marca in dict :
            dict[marca] = []
        if vendedor not in dict[marca] :
            dict[marca].append(vendedor)
            
    marca  = []
    distribucion = [] 
    for vendedor in dict:
        marca.append(vendedor)
        distribucion.append(len(dict[vendedor]))
    
    posiciones = ordenar(distribucion)    
    dict = {}
    
    for pos in posiciones[:N] :
        dict[marca[pos]] = distribucion[pos]
    return dict
            
if __name__ == '__main__' :
    data = catalog.read_catalog()
    """
    puede descomentar las siguientes llamadas para ver los resultados
    """    
    reportar(data)
    #Ejercicio 1
    #print(obtener_vendedores_y_productos(data))
    #Ejercicio 2
    #print(obtener_mejores_vendedores(data))
    #Ejercicio 3
    #print(obtener_variacion_productos(data) )
    #Ejercicio 4
    #print(obtener_vendedores_por_producto(data, 'AVpfUsrxLJeJML437Ezd'))
    #Ejercicio 5
    #print(obtener_vendedor_mas_barato(data, 'AVpfUsrxLJeJML437Ezd'))    
    #Ejercicio 6
    print(obtener_mejores_marcas(data, 5))
