"""
Ejericio 1.
Determinar si un string corresponde a un entero válido
"""

entero_str = input('Ingrese un entero válido: ')

len_str = len(entero_str)
i = 0
while i < len_str  and  entero_str[i]>='0' and entero_str[i]<='9' :
    i = i + 1

if i == len_str :
    print('válido')
else :
    print('inválido')
      
    