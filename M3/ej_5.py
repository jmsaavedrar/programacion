"""
Ordenar por comunas
"""
def ordenar_por_comunas(nombres, comunas):
    n = len(nombres)
    for i in range(n - 1):
        menor = comunas[i]
        pos = i
        for j in range(i+1, n):
            if comunas[j] < menor:                
                menor = comunas[j]
                pos = j
        
        #mueve las comunas
        comunas[pos] = comunas[i]
        comunas[i] = menor
        
        #mueve los nombres
        aux = nombres[pos]
        nombres[pos] = nombres[i]
        nombres[i] = aux
        

def crear_listas_por_comunas(usuarios, comunas):
    comunas_unicas = []
    lista_por_comunas = []    
    n=len(comunas)
    i = 0
    j = 0
    while i < n :
        comuna = comunas[i]
        comunas_unicas.append(comuna)
        lista_por_comunas.append([usuarios[i]])
        i = i + 1
        while i < n and comuna == comunas[i]:            
            lista_por_comunas[j].append(usuarios[i])
            i = i + 1 
        j = j + 1
    return comunas_unicas, lista_por_comunas    
    


personas = ['Juan', 'Ana', 'Pedro', 'Camila', 'Julio', 'María']
comunas = ['Las Condes', 'Ñuñoa', 'Providencia', 'Las Condes', 'Ñuñoa', 'La Florida']


print('--------------input--------------------')
print('personas: {}'.format(personas))
print('comunas: {}'.format(comunas))
ordenar_por_comunas(personas, comunas)
comunas_unicas, grupos = crear_listas_por_comunas(personas, comunas)
print('--------------------output--------------')
for i, comuna in enumerate(comunas_unicas):
    print('Comuna: {}'.format(comuna))
    print(grupos[i])

