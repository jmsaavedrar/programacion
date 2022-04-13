"""
Ejericio 1.
Determinar si un string corresponde a un entero válido
"""

entero_str = input('Ingrese un entero válido: ')
len_str = len(entero_str)
valido = True
i = 0

while i < len_str and valido == True :
    if entero_str[i]>='0' and entero_str[i]<='9' :
        i = i + 1
    else :
        valido = False

if valido == True :
    entero = int(entero_str)
    print('el valor sí es entero ', entero)
else :    
    print('dato no válido')    
    