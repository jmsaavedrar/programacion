"""
Ordenar por comunas
"""
def ordenar_por_comunas(usuarios, comunas):
    n = len(usuarios)
    for i in range(n - 1):
        menor = comunas[i]
        pos = i
        for j in range(i+1, n):
            if comunas[j] < menor:                
                menor = comunas[j]
                pos = j
        
        menor_usuario = usuarios[pos]
        usuarios[pos] = usuarios[i]
        usuarios[i] = menor_usuario                
        comunas[pos] = comunas[i]
        comunas[i] = menor

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
    
#def crear_lista_por_comunas(usuario, comunas):
#    comunas_unicas = []
#    usuarios_por_comuna = []

usuarios = ['Juan', 'Ana', 'Pedro', 'Camila', 'Julio']
comunas = ['A', 'B', 'A', 'C', 'B']

ordenar_por_comunas(usuarios, comunas)
print(usuarios)
print(comunas)
comunas_unicas, lista = crear_listas_por_comunas(usuarios, comunas)
print(comunas_unicas)
print(lista)

