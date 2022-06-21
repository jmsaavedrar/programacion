"""

crearemos una lista de diccionario de estudiantes
un estudiante

 { 'nombre' : string
   'edad' : int
   'carrera' : string
 }
"""
import matplotlib.pyplot as plt

estudiantes = []

f = open('lista_estudiantes.txt')

for linea in f :
    linea_1 = linea.strip()
    linea_1 = linea_1.split(',')    
    estudiantes.append({'nombre': linea_1[0],
                        'edad': int(linea_1[1]),
                        'carrera': linea_1[2],                        
                         })
    
f.close()


def contar_por_carrera(lista_estudiantes, campo):
    dic = {}
    for item in lista_estudiantes :
        if not item[campo] in dic :
            dic[item[campo]] = 1
        else :
            dic[item[campo]] += 1
    return dic


for estudiante in estudiantes:
    print(estudiante)
print('estadísticas')
print('------------------')
dic = contar_por_carrera(estudiantes, 'carrera')
print(dic)

# carreras  = []
# frecuencias = []
# for key in dic :
#     carreras.append(key)
#<     frecuencias.append(dic[key])
carreras = [key for key in dic]
frecuencias = [dic[key] for key in dic]

print(carreras)
print(frecuencias)
plt.bar(carreras, frecuencias)
plt.show()

