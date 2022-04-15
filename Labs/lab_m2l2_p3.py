"""
Laboratorio M2L2
num2tex
Parte 3, agregamos menos
"""



txt_unidades = ['',
            'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve',
            'diez', 'once', 'doce', 'trece', 'catorce', 'quince', 'dieciséis', 'diecisiete', 'dieciocho', 'diecinueve',
            'veinte', 'veintiuno', 'veintidos', 'vieintitres', 'veinticuatro', 'veinticinco', 'veintiséis', 'veintisiete', 'veintiocho', 'veintinueve'] 

txt_decenas = ['','', '', 'treinta', 'cuarenta', 'cincuenta', 'sesenta', 'setenta', 'ochenta', 'noventa']
txt_centenas = ['', 'ciento','doscientos','trescientos', 'cuatrocientos', 'quinientos', 'seiscientos', 'setecientos', 'ochocientos', 'novecientos']

txt_miles = ['', 'mil']
txt_millones = ['', 'millones']

numero = int(input('Ingrese cantidad: '))

prefijo = ''
if numero < 0 :
    prefijo = 'menos '
    numero = numero * -1
    
texto = ''
it_millones = 0 
#dividimos en grupos de 6 cifras
while numero >  0 :
    numero_6cifras = numero % 1000000
    numero = numero// 1000000
    texto_6cifras = ''
    it_miles = 0
    #leemos cada grupo de 6, y traducimos
    while numero_6cifras > 0 :                
        #traducimos cada 3 cifras
        numero_3cifras = numero_6cifras % 1000
        numero_6cifras = numero_6cifras // 1000 
        #extraemos las 2 últimas cifras
        unidades = numero_3cifras % 100
        centenas = numero_3cifras // 100        
        texto_3cifras = ''
        if unidades >= 30 :
            decenas = unidades // 10
            unidades = unidades % 10      
            texto_unidades = txt_unidades[unidades]
            if (it_miles > 0 or it_millones) > 0 and unidades == 1:
                texto_unidades = 'un'
            if texto_unidades == '' :
                texto_3cifras =  txt_decenas[decenas]
            else :
                texto_3cifras =  txt_decenas[decenas] + ' y ' + texto_unidades
                
        else : 
            texto_3cifras = txt_unidades[unidades]
            if (it_miles > 0 or it_millones > 0) and (unidades == 1 or unidades == 21):
                if unidades == 1 :
                    texto_3cifras = 'un'
                if unidades == 21 :
                    texto_3cifras = 'veintiun'                
            
        if centenas > 0 :
            if texto_3cifras == '' and centenas == 1 :
                texto_3cifras = 'cien'
            else:
                texto_3cifras = txt_centenas[centenas] + ' ' + texto_3cifras
        #texto_3cifras tiene el texto de grupos de 3   
        if it_miles == 1 and texto_3cifras == 'un' :
            texto_6cifras = 'mil ' + texto_6cifras
        else :
            texto_6cifras = texto_3cifras + ' ' + txt_miles[it_miles] + ' ' + texto_6cifras
        it_miles = it_miles + 1
    texto = texto_6cifras + ' ' + txt_millones[it_millones] + ' ' + texto
    it_millones = it_millones + 1

if prefijo != '':
    texto = prefijo + ' ' +  texto                     
print('Traducción: ', texto)



