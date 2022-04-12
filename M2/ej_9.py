"""
"""

intentos = 0
passwd="x"
passwd1=""
while passwd != passwd1 and intentos < 3:    #while passwd1 vs passwd
    print('intentos : ', intentos + 1)
    hay_digito = False
    while not hay_digito:
        passwd = input('Ingrese contraseña: ') # while passwd válido
        i = 0
        while i < len(passwd)  and  not hay_digito : # while check
            if passwd[i]>='0' and passwd[i]<='9' :
                hay_digito = True
            else :
                i = i + 1                         
    passwd1 = input('Reingrese contraseña: ')
    intentos = intentos + 1
    
if passwd == passwd1 :
    print('{} {}'.format(passwd, passwd1) )
    print('contraseña correcta!!!')
else :
    print('Error al procesar contraseña')




