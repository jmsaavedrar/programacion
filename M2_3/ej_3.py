"""
ordenar
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

print(nombres)
