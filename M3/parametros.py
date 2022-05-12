"""
Tuplas
"""
def obtener_mayor_menor(lista) :
    mayor = lista[0]
    menor = lista[0]
    n = len(lista)
    for i in range(1, n):
        if lista[i] > mayor :
            mayor = lista[i]
        if lista[i] < menor :
            menor = lista[i]
    return (mayor, menor)


A = [10, 5, 100, 4, 1000, 1, 6000, 0]
#tupla = obtener_mayor(A)
#print('mayor: {}'.format(tupla[0]))
#print('menor: {}'.format(tupla[1]))
ma, me = obtener_mayor_menor(A)
print('mayor: {}'.format(ma))
print('menor: {}'.format(me))








            





