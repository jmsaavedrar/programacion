"""
Ejercicio 5 implementado con diccionarios
"""

personas = ['Juan', 'Ana', 'Pedro', 'Camila', 'Julio', 'María']
comunas = ['Las Condes', 'Ñuñoa', 'Providencia', 'Las Condes', 'Ñuñoa', 'La Florida']

def crear_listas_por_comunas(personas, comunas) :
    dic = {}
    for i, comuna in enumerate(comunas) :
        if comuna in dic :
            dic[comuna].append(personas[i])
        else :
            dic[comuna] = [personas[i]]
    return dic 

print('--------------input--------------------')
print('personas: {}'.format(personas))
print('comunas: {}'.format(comunas))
mi_dic = crear_listas_por_comunas(personas, comunas)
print('--------------------output--------------')
for key in mi_dic:
    print('Comuna: {}'.format(key))
    print(mi_dic[key])
