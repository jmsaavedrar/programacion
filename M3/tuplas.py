
def mayor_menor(lista):
    mayor = 0
    menor = 1
    return mayor, menor

def crear_lista():
    a = []
    a.append({'nombre': 'Juan', 'edad': 27, 'nota': 6})
    a.append({'nombre': 'Pedro', 'edad': 18, 'nota': 5})
    a.append({'nombre': 'Camila', 'edad': 20, 'nota': 7})
    return a

def reportar(a):
    for item in a :
        print(item['nombre'])


def ordenar(lista, field):
    n = len(lista)
    for i in range(n - 1):
        menor = lista[i]
        pos = i
        for j in range(i+1, n):
            if lista[j][field] < menor[field]:
                menor = lista[j]
                pos = j
        lista[pos] = lista[i]
        lista[i] = menor
#x = mayor_menor([])

#print(x)


#reportar(crear_lista())

#xx= list(enumerate([1,2,3]))
#print(xx[0][0])
def ff(x):
    x = x  + 1
    print(id(x))
    return x

def gg(x):
    x = [1,2,3]    
    print(id(x))    


    
if __name__ == '__main__':
    # x = 5
    # z = ff(x)
    # print(x)
    # print(id(x))
    # print(type(x))
    # a = []
    # gg(a)
    # print('{} {}'.format(id(a),a))

    A = crear_lista()
    ordenar(A, 'nota')
    print(A)
