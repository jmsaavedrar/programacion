"""
MyPet
"""

dic_pets = [
    {'id':1, 'nombre': 'Bob',  'edad': 2, 'tipo': 'Gato', 'raza': 'Esfinge',  'comuna' : 'Santiago',  'estado': 1},
    {'id':2, 'nombre': 'Tom',  'edad': 2, 'tipo': 'Gato', 'raza': 'Siberiano','comuna' : 'Ñuñoa',     'estado': 1},
    {'id':3, 'nombre': 'Babe', 'edad': 4, 'tipo': 'Perro', 'raza': 'Dalmata',  'comuna' : 'Las Condes','estado': 1},
    {'id':4, 'nombre': 'Kid',  'edad': 6, 'tipo': 'Perro', 'raza': 'Pastor',   'comuna' : 'Las Condes','estado': 0 },
    {'id':5, 'nombre': 'Solo', 'edad': 5, 'tipo': 'Perro', 'raza': 'Poodle',   'comuna' : 'La Florida','estado': 1}    
    
    ]


def reportar(dic_pets):
    for item in dic_pets:
        print('id: {} '.format(item['id']))
        print('nombre: {} '.format(item['nombre']))
        print('edad: {} '.format(item['edad']))
        print('tipo: {} '.format(item['tipo']))
        print('raza: {} '.format(item['raza']))
        print('comuna: {} '.format(item['comuna']))
        print('estado: {} '.format(item['estado']))
        print('***************************************************')
        

def reportar_por_ids(dic_pets, ids):
    for i in ids:
        item = dic_pets[i]
        print('id: {} '.format(item['id']))
        print('nombre: {} '.format(item['nombre']))
        print('edad: {} '.format(item['edad']))
        print('tipo: {} '.format(item['tipo']))
        print('raza: {} '.format(item['raza']))
        print('comuna: {} '.format(item['comuna']))
        print('estado: {} '.format(item['estado']))
        print('***************************************************')
        
#1
def contar(dic_pets):
    dic_cantidades = {'Perro': 0, 'Gato': 0}
    for item in dic_pets:
        dic_cantidades[item['tipo']] = dic_cantidades[item['tipo']] + 1 
    return dic_cantidades

#2
def contar_mascotas_perdidas_por_comuna(dic_pets):
    dic = {}
    for item in dic_pets:
        dic[item['comuna']] = 0
        
    for item in dic_pets:
        if item['estado'] == 1 :
            dic[item['comuna']] = dic[item['comuna']] + 1 
    return dic
#3
def obtener_ids_mascotas_por_comuna(dic_pets, comuna) :
    ids = []
    for item in dic_pets:
        if item['estado'] == 1 and item ['comuna'] == comuna:
            ids.append(item['id'])
    return ids

#4
def obtener_promedio_edades_por_comuna(dic_pets):
    dic = {}
    for item in dic_pets:
        dic[item['comuna']] = []
        
    for item in dic_pets:
        dic[item['comuna']].append(item['edad'])
        
    for key in dic:
        s = 0
        for edad in dic[key] : 
            s = s + edad
        if len(dic[key]) > 0 :
            dic[key] = s / len(dic[key])       
    return dic

#5
def  contar_mascotas_encontradas_por_comuna(dic_pets):
    dic = {}
    for item in dic_pets:
        dic[item['comuna']] = 0
        
    for item in dic_pets:
        if item['estado'] == 0 :
            dic[item['comuna']] = dic[item['comuna']] + 1
    return dic

def actualizar_mascota_a_encontrado(dic_pets, lista_ids) :
    for item in dic_pets:
        if item['id'] in lista_ids:
            item['estado'] = 0

def contar_perro_y_gatos_por_comuna(dic_pets):
    dic = {}
    for item in dic_pets:
        dic[item['comuna']] = {'Perro': 0, 'Gato':0}
    
    for item in dic_pets:
        dic[item['comuna']][item['tipo']] = dic[item['comuna']][item['tipo']] + 1  
    
    return dic
#print(contar(dic_pets))
#print(contar_mascotas_perdidas_por_comuna(dic_pets))
#print(obtener_ids_mascotas_por_comuna(dic_pets, 'Santiago'))
#print(obtener_promedio_edades_por_comuna(dic_pets))
#actualizar_mascota_a_encontrado(dic_pets, [1]) 
#print(contar_mascotas_encontradas_por_comuna(dic_pets))
#print(contar_perro_y_gatos_por_comuna(dic_pets))