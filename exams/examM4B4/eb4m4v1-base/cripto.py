"""
"""
import matplotlib.pyplot as plt
def load_file(filename):
    f = open(filename)    
    lines = f.readlines()[1:]
    data = []
    for line in lines :
        ldata = line.strip().split(',')
        date_time = ldata[3].split()
        data.append({ 
            'nro' : int(ldata[0]),
            'name' : ldata[1],
            'symbol' : ldata[2],
            'fecha' : date_time[0],
            'time' :date_time[1],
            'high' : float(ldata[4]),
            'open' : float(ldata[5]),
            'close' : float(ldata[6]),
            'volume' : float(ldata[6]),
            'mktcap' : float(ldata[7])            
            }
            )
    f.close()
    return data

def reportar(data):
    for item in data:
        print(item)

def aumentar_fecha(año, mes, dia):
    año_s = año
    mes_s = mes
    dia_s = dia + 1    
    if mes == 2 and dia ==  28 :
        dia_s = 1
        mes_s = mes + 1 
    elif mes in [1,3,5,7,8,10,12] and dia == 31 :
        dia_s = 1
        mes_s = mes + 1
        
    elif mes in [4,6,9,11] and dia == 30  :
        dia_s = 1
        mes_s = mes + 1
    
    if mes_s == 13 :
        año_s = año +1
        mes_s = 1    

    return (año_s, mes_s, dia_s)

def pad_zero(val):
    string =''
    if val <10 :
        string = '0{}'.format(val)
    else:
        string = '{}'.format(val)
    return string

def obtener_fechas(fecha, dias):
    año_mes_dia = fecha.split('-')
    año = int(año_mes_dia[0])
    mes = int(año_mes_dia[1])
    dia = int(año_mes_dia[2])
    
    fechas = []
    fechas.append('{}-{}-{}'.format(año, pad_zero(mes), pad_zero(dia)))
    for i in range(dias-1):
        año_s, mes_s, dia_s = aumentar_fecha(año, mes, dia)
        fechas.append('{}-{}-{}'.format(año_s, pad_zero(mes_s), pad_zero(dia_s)))
        año = año_s
        mes = mes_s
        dia = dia_s
    return fechas
    
    
def  obtener_high_value(data):
    dict = {}
    for item in data:
        dict[item['fecha']] = item['high']
    return dict
    
def obtener_high_values_fechas(data, fechas):
    vals = []
    dict = obtener_high_value(data)
    
    for i in range(len(fechas)) :
        vals.append(0)
        
    for i,fecha in enumerate(fechas) :
        if fecha in  dict:
            vals[i] = dict[fecha]
            
    return vals

def obtener_signo_alta_baja(data):    
    dict = {}
    dict[data[0]['fecha']] = 0
    for i in range(1, len(data)) :
         dict[data[i]['fecha']] = data[i]['high']  - data[i-1]['high']
    return dict

def obtener_nro_alzas_bajas(data, fechas):
    dict = obtener_signo_alta_baja(data)
    alzas = 0
    bajas = 0
    for fecha in fechas:
        if fecha in dict :
            if dict[fecha] > 0 :
                alzas += 1
            if dict[fecha] < 0 :
                bajas += 1
    return (alzas, bajas)
data_eth = load_file('ETH.csv')
data_btc = load_file('BTC.csv')
#reportar(data)
#fechas = obtener_fechas('2013-04-29', 7)
# vals = obtener_high_values_fechas(data, fechas)
# plt.plot(fechas, vals)
# print(fechas)
# print(vals)

fechas = obtener_fechas('2019-01-12', 30)
alzas, bajas = obtener_nro_alzas_bajas(data_eth, fechas)
alzas_btc, bajas_btc = obtener_nro_alzas_bajas(data_btc, fechas)
print('{} {}'.format(alzas, bajas))
fig, hs = plt.subplots(1,2)
hs[0].bar(['alzas', 'bajas'], [alzas, bajas], color = 'blue')
hs[0].set_xlabel('ETH')
hs[1].bar(['alzas', 'bajas'], [alzas_btc, bajas_btc], color = (1,0,0))
hs[1].set_xlabel('BTC')
plt.show()