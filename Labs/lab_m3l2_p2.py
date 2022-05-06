
"""
Ordenar por comunas
"""

def crear_listas_por_comunas(comunas):
    dic = {}        
    i = 0
    j = 0
    for i, comuna in enumerate(comunas) :
        if comuna in dic :
            dic[comuna].append(i)
        else :
            dic[comuna] = [i]
    return dic    
    
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
dic_grupos = crear_listas_por_comunas(comunas_estudiante)
print('--------------------output--------------')
for comuna in dic_grupos :
    print('*******************')
    print('COMUNA: {}'.format(comuna))
    print('*******************')
    print('--- ESTUDIANTES:')
    for idx in dic_grupos[comuna] :
        print('----- {} {}'.format(nombres_estudiante[idx], notas_estudiante[idx]))
    print('---PROMEDIO: {}'.format(round(calcular_promedio(notas_estudiante, dic_grupos[comuna]), 2)))

    
