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
 
        
    return dict 
        
def ordenar(A):
    posiciones = []
    
                            
    return posiciones
            
def obtener_mejores_vendedores(data): 
    dict = obtener_vendedores_y_productos(data)

        
    nuevo_dict = {}
    
    return nuevo_dict
        
def obtener_variacion_productos(data) :
    dict = {}
    
    return  dict
    
                      
def obtener_vendedores_por_producto(data, id) :
    dict = {}

    return dict

def obtener_pos_menor(valores):
    pos = 0
  
    return pos

def obtener_vendedor_mas_barato(data, id) :    
    dict = {}
    return dict 

def obtener_mejores_marcas(data, N) :
    dict = {}
    
    return dict
            
if __name__ == '__main__' :
    data = catalog.read_catalog()
    """
    puede descomentar las siguientes llamadas para ver los resultados
    """    
    #reportar(data)
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
