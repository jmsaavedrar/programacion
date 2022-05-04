"""
Filtrar por edad
"""

def filtrar_por_edad(nombres, edades, edad_corte):
    filtrado = []
    for i, edad in enumerate(edades) :
        if edad >= edad_corte :
            filtrado.append(nombres[i])
    return filtrado
    
nombres = ['Juan', 'Ana', 'Pedro', 'Camila']
edades = [18, 17, 20, 21]
nueva_lista = filtrar_por_edad(nombres, edades, 20)
print(nueva_lista)


