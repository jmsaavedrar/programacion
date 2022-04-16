"""
no digitos consecutivos
"""
passwd = input('Ingrese contraseña: ')

valido = True

N = len(passwd)
i = 0
while i < N - 1 and valido:
    if passwd[i].isdigit() and passwd[i + 1].isdigit() :
        if int(passwd[i + 1]) - int(passwd[i]) == 1 :
            valido = False
    i = i + 1
    
if valido :
    print('válido')      
else :    
    print('no válido')


    