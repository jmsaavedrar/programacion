"""
buscar por apellido
Ingrese apellido, sale cuando se ingresa "SALIR"
"""
n_nombres = int(input('N :'))
nombres = []
apellidos = []
for i in range(n_nombres) :
    nombre = input('nombre {}: '.format(i+1))
    apellido = input('apellido {}: '.format(i+1))
    nombres.append(nombre)
    apellidos.append(apellido)
    
apellido= input('Apellido a buscar: ')

while apellido.upper() != 'SALIR' :
    for i in range(n_nombres) :
        if apellidos[i].find(apellido) != -1 :
            print('{},  {}'.format(nombres[i], apellidos[i]))

    apellido= input('Apellido a buscar: ')
            
print('fin')            