"""
no acepta repetidos
"""
n_nombres = int(input('N :'))
nombres = []
i = 0 
while i < n_nombres :
    
    nombre = input('nombre {}: '.format(i+1))
    while nombre in nombres :
        print('error: {} ya existe, ingrese nuevamente')
        nombre = input('nombre {}: '.format(i+1))
    nombres.append(nombre)
    i = i + 1
print(nombres)
