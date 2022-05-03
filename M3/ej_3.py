"""
dec2bin
Imprimir el binario de los primeros números en base 10
"""

def dec2bin(dec) :
    str_bin = ''
    if dec == 0 :
        str_bin = '0'
    while dec != 0 :
        r = dec % 2
        str_bin = str(r) +  str_bin
        dec = dec // 2
    return str_bin


N = int(input('N:'))

for numero in range(N) :
    binario = dec2bin(numero)
    print('{} -> {}'.format(numero, binario))