"""
¿Es binario?
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


bin_input = input('Ingrese nro binario:')

if es_binario(bin_input) :
    print('{} es binario'.format(bin_input))
else:
    print('{} no es binario'.format(bin_input))
    