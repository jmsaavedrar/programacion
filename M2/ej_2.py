"""
Ejericio 1.
Determinar si un string corresponde a un flotante válido
"""
real_str = input('Ingrese un real válido: ')

len_str = len(real_str)
i = 0
while i < len_str  and  real_str[i]>='0' and real_str[i]<='9' :
    i = i + 1

if i < len_str  and (real_str[i] == '.' or (real_str[i]>='0' and real_str[i]<='9')) :
    i = i  +1 
    
while i < len_str  and  real_str[i]>='0' and real_str[i]<='9' :
    i = i + 1
    
if i == len_str :
    print('válido')
else :
    print('inválido')
      
    