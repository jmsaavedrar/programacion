"""
buscar por apellido
"""
n_nombres = int(input('N :'))
nombres = []
for i in range(n_nombres) :
    nombre = input('nombre {}: '.format(i+1))
    nombres.append(nombre)
    
apellido= int(input('Apellido a buscar'))