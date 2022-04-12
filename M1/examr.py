"""
examen recuperativo
solución parte 4
"""

p_rango_1 = float(input('ingrese probilidad 1: '))
p_rango_2 = float(input('ingrese probilidad 2: '))
p_rango_3 = float(input('ingrese probilidad 3: '))
p_rango_4 = float(input('ingrese probilidad 4: '))
p_rango_5 = float(input('ingrese probilidad 5: '))
p_rango_6 = float(input('ingrese probilidad 6: '))

suma = p_rango_1 +  p_rango_2 + p_rango_3 + p_rango_4 + p_rango_5 + p_rango_6
suma = round(suma, 2)
p_aprob = p_rango_4 + p_rango_5 + p_rango_6
p_aprob  = round(p_aprob, 2)
print('Es distribución válida: ', suma == 1.0)
print('La probabilidad de aprobar es:', p_aprob ) 