"""
dec2bin
"""

dec = int(input('Ingrese nro: '))
str_bin = ''
if dec == 0 :
    str_bin = '0'
while dec != 0 :
    r = dec % 2
    str_bin = str(r) +  str_bin
    dec = dec // 2

print(str_bin)
print('Se requieren {} bits'.format(len(str_bin)))

