"""
Ordenar por comunas
"""
#Ordenamos las tres listas
def ordenar_por_comunas(nombres, notas, comunas):
    n = len(comunas)
    for i in range(n - 1):
        menor = comunas[i]
        pos = i
        for j in range(i+1, n):
            if comunas[j] < menor:                
                menor = comunas[j]
                pos = j
        
        
        #movemos las comunas
        comunas[pos] = comunas[i]
        comunas[i] = menor
        
        #movemos los nombres
        menor = nombres[pos]
        nombres[pos] = nombres[i]
        nombres[i] = menor             
           
        #movemos las notas
        menor = notas[pos]
        notas[pos] = notas[i]
        notas[i] = menor          
        

def crear_listas_por_comunas(comunas):
    comunas_unicas = []
    idx_por_comunas = []    
    n=len(comunas)
    i = 0
    j = 0
    while i < n :
        comuna = comunas[i]
        comunas_unicas.append(comuna)
        idx_por_comunas.append([i])
        i = i + 1
        while i < n and comuna == comunas[i]:            
            idx_por_comunas[j].append(i)
            i = i + 1 
        j = j + 1
    return comunas_unicas, idx_por_comunas    
    
def calcular_promedio(notas, grupo):
    suma = 0    
    for idx in grupo :
        suma = suma + notas[idx]
    return suma / len(grupo)
    

nombres_estudiante = ['Juan', 'Ana', 'Camila', 'Rodrigo', 'Pedro', 'Violeta', 'Claudia', 'Sebastián', 'Andrés', 'Luis']
comunas_estudiante = ['Las Condes', 'Providencia', 'La Florida', 'Las Condes', 'La Florida', 'Ñuñoa', 'Las Condes', 'Ñuñoa', 'Las Condes', 'Providencia']
notas_estudiante = [5,7,6.3, 4.6, 5.8, 6.7, 6.5, 5.2, 4.6, 6.0, 5.2]

print('--------------input--------------------')
print('personas: {}'.format(nombres_estudiante))
print('comunas: {}'.format(comunas_estudiante))
ordenar_por_comunas(nombres_estudiante, notas_estudiante, comunas_estudiante)
comunas_unicas, grupos = crear_listas_por_comunas(comunas_estudiante)
print('--------------------output--------------')
for i, grupo in enumerate(grupos) :
    print('*******************')
    print('COMUNA: {}'.format(comunas_unicas[i]))
    print('*******************')
    print('--- ESTUDIANTES:')
    for idx in grupo :
        print('----- {} {}'.format(nombres_estudiante[idx], notas_estudiante[idx]))
    print('---PROMEDIO: {}'.format(round(calcular_promedio(notas_estudiante, grupo), 2)))

    
