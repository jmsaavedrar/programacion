
"""
Se presenta una lista de dicctionarios, 
donde cada diccionario representa a un producto

"""
import matplotlib.pyplot as plt
#Leer datos de catálogo
def read_catalog() :
    f = open('ecommerce.csv')    
    datalist = f.readlines()
    data = []
    for item in datalist[1:]:
        l = item.strip().split(',')        
        data.append({'id' : l[0],  
         'precio_max' : float(l[1]),
         'precio_min' : float(l[2]),
         'vendedor' : l[3],
         'marca' : l[4],
         'descripcion' : l[5],
         'peso': l[6]})                   
    return data

def ordenar(dict):
    dic_ordenado = sorted(dict.items(), key = lambda x : x[1], reverse = True)
    return dic_ordenado

#Mostrar los 10 vendedores con más productos

#1
def top_vendedores(data, N):
    return 0
#2
def top_marcas(data, N):
    return 0
#3
def top_marcas_precio(data, N):
    return 0
#4
def top_marcas_vendedor(data, N):
    return 0
#5
def top_vendedor_productos_precio(data, N, M):
    return 0
    

def reportar(data):
    for item in data:
        print(item)    
            
#5 
data = read_catalog()
#reportar(data))
#1
#print(top_vendedores(data, 5))
#2
#print(top_marcas(data, 5))
#3
#print(top_marcas_precio(data, 5))
#4
#print(top_marcas_vendedor(data, 5))
#5
print(top_vendedor_productos_precio(data, 5, 3))
        
    
