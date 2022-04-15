"""
Laboratorio M2L2
num2tex
Parte 1
"""



txt_unidades = ['',
            'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve',
            'diez', 'once', 'doce', 'trece', 'catorce', 'quince', 'dieciséis', 'diecisiete', 'dieciocho', 'diecinueve',
            'veinte', 'veintiuno', 'veintidos', 'vieintitres', 'veinticuatro', 'veinticinco', 'veintiséis', 'veintisiete', 'veintiocho', 'veintinueve'] 

txt_decenas = ['','', '', 'treinta', 'cuarenta', 'cincuenta', 'sesenta', 'setenta', 'ochenta', 'noventa']
txt_centenas = ['', 'ciento','doscientos','trescientos', 'cuatrocientos', 'quinientos', 'seiscientos', 'setecientos', 'ochocientos', 'novecientos']

numero = int(input('Ingrese cantidad: '))
#extraemos las 2 últimas cifras
unidades = numero % 100
centenas = numero // 100
if unidades >= 30 :
    decenas = unidades // 10
    unidades = unidades % 10      
    texto =  txt_decenas[decenas] + ' y ' + txt_unidades[unidades]
else :
    texto = txt_unidades[unidades]

if centenas > 0 :
    if texto == '' and centenas == 1 :
        texto = 'cien'
    else:
        texto = txt_centenas[centenas] + ' ' + texto

print('Traducción: ', texto)



