
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
def obtener_vendedores_productos(data):
    # vendedor : cantidad
    dic_conteo = {}
    for item in data :
        vendedor = item['vendedor']
        if vendedor in dic_conteo :
            dic_conteo[vendedor] += 1
        else :
            dic_conteo[vendedor] = 1
    return dic_conteo

def obtener_marcas_productos(data):
    # vendedor : cantidad
    dic_conteo = {}
    for item in data :
        marca = item['marca']
        if marca in dic_conteo :
            dic_conteo[marca] += 1
        else :
            dic_conteo[marca] = 1
    return dic_conteo

def obtener_marcas_mayor_precio(data):
    dic_precio = {}
    for item in data :
        marca = item['marca']
        precio = item['precio_max']
        if marca in dic_precio :
            if precio > dic_precio[marca]: 
                dic_precio[marca] = precio
        else :
            dic_precio[marca] = precio
    return dic_precio


def obtener_marcas_vendedores(data):
    # vendedor : cantidad
    dic = {}
    for item in data :
        marca = item['marca']
        vendedor = item['vendedor'] 
        if not marca in dic :
            dic[marca] = []
        if not vendedor in dic[marca] :
            dic[marca].append(vendedor)
    for marca in dic :
        dic[marca] = len(dic[marca])
    return dic


def obtener_vendedor_productos_caros(data):
    dic = {}
    for item in data :
        vendedor = item['vendedor']
        id = item['id']
        precio = item['precio_max']
        if not vendedor in dic :
            dic[vendedor] = {}        
        dic[vendedor][id] = precio
    return dic    

#1
def top_vendedores(data, N):
    dic = obtener_vendedores_productos(data)
    return ordenar(dic)[:N]
#2
def top_marcas(data, N):
    dic = obtener_marcas_productos(data)
    return ordenar(dic)[:N]
#3
def top_marcas_precio(data, N):
    dic = obtener_marcas_mayor_precio(data)
    return ordenar(dic)[:N]
#4
def top_marcas_vendedor(data, N):
    dic = obtener_marcas_vendedores(data)
    return ordenar(dic)[:N]
#5
def top_vendedor_productos_precio(data, N, M):
    dic = obtener_vendedor_productos_caros(data)
    dic_precios = {}
    for vendedor in dic :
        dic[vendedor] = ordenar(dic[vendedor])
        #print(dic[vendedor])
        dic_precios[vendedor] = dic[vendedor][0][1]
    ordenado_por_precio = ordenar(dic_precios)
    #print(ordenado_por_precio[:10])
    result = {}
    for item in ordenado_por_precio[:N] :
        result[item[0]] = dic[item[0]][:M]
    
    return result    
    

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
        
    