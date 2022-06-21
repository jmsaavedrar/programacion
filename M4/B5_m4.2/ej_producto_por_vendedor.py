"""
Ejemplo lectura de archivos  y gráfico de barras
"""
import matplotlib.pyplot as plt
 
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

def obtener_max(lista):
    maxv = lista[0]
    for i in range(len(lista)) :
        if lista[i] > maxv :
            maxv = lista[i]
    return maxv        

def productos_por_vendedor(data):
    # vendedor : cantidad
    dic_conteo = {}
    for item in data :
        vendedor = item['vendedor']
        if vendedor in dic_conteo :
            dic_conteo[vendedor] += 1
        else :
            dic_conteo[vendedor] = 1
    return dic_conteo
######

data = read_catalog()
conteo = productos_por_vendedor(data) 
print(conteo)   

# keys = []
# values = []
# for key in conteo :
#     keys.append(key)
#     values.append(conteo[key])
keys = list(conteo.keys())
values = list(conteo.values())
#Imprime las primeras10 respuestas sin importar el orden
keys = keys[0:10]
values = values[0:10] 
plt.bar(keys, values)
#rota los textos en el eje x
plt.xticks(rotation = 45) 
plt.show()
    
# precios = []
# for item in data :
#     precios.append(item['precio_max'])
# maxv = obtener_max(precios)
# print(maxv)        
    


