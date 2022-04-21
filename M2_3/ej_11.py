"""
bin2dec
"""

str_bin = input('Ingrese binario: ')

n = len(str_bin)
dec = 0
for i in range(n-1,-1, -1):
    dec = dec + 2**(n-1-i)*int(str_bin[i])

print(dec)