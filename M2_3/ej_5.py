"""
nro de ocurrencias
"""
n_nombres = int(input('N :'))
nombres = []
for i in range(n_nombres) :
    nombre = input('nombre {}: '.format(i+1))
    nombres.append(nombre)


for i in range(n_nombres - 1):
    menor = nombres[i]
    pos = i
    for j in range(i+1, n_nombres):
        if nombres[j] < menor:
            menor = nombres[j]
            pos = j
    nombres[pos] = nombres[i]
    nombres[i] = menor

nombres_unicos = []
ocurrencias = []

i = 0
j  = 0 #contabiliza la cantidad de nombres únicos
while i < n_nombres :     
    nombres_unicos.append(nombres[i])
    ocurrencias.append(1)
    i = i + 1
    while i < n_nombres and nombres_unicos[j] == nombres[i] :
        ocurrencias[j] = ocurrencias[j] + 1 
        i = i + 1
    j = j + 1
n_nombres_unicos = j
for i in range(n_nombres_unicos) :
    print('{}: {} ocurrencias'.format(nombres_unicos[i], ocurrencias[i]))
    