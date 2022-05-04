"""
bin2dec
"""

def es_binario(mi_input):
    binario = True
    i = 0
    n = len(mi_input)
    while binario and i < n :
        if mi_input[i] != '0' and mi_input[i] != '1' :
            binario = False
        i = i + 1
    return binario  


def bin2dec(str_bin):
    n = len(str_bin)
    dec = 0
    for i in range(n-1,-1, -1):
        dec = dec + 2**(n-1-i)*int(str_bin[i])
    return dec

A = ['10001', '00011', '1111', '10000001', '123', '01010101']

print(A)

for item in A :
    if es_binario(item) :
        print('{} -> {}'.format(item, bin2dec(item)))
    else :
        print('{} no es binario'.format(item))
        
