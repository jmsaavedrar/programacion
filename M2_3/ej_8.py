"""
buscar por apellido
"""
n_nombres = int(input('N :'))
nombres = []
apellidos = []
for i in range(n_nombres) :
    nombre = input('nombre {}: '.format(i+1))
    apellido= input('apellido {}: '.format(i+1))
    nombres.append(nombre)
    apellidos.append(apellido)
    
apellido= input('Apellido a buscar: ')

for i in range(n_nombres) :
    if nombres[i].find(apellido) != -1 :
        print(nombres[i])

