"""
Tarea 3 B4
"""




def reportar(lista_dic, posiciones):
    for pos in posiciones :
        print(lista_dic[pos])         


def menu():
    print('***********************************')
    print('**           AUTOSCLS            **')
    print('***********************************')
    print('|                                 |')
    print('|       1. Reportar               |')
    print('|       2. Filtrar                |')
    print('|       3. Estadísticas           |')
    print('|       4. Salir                  |')
    print('|                                 |')
    print('|       Elija Opcion              |')
    print('|                                 |')
    print('|_________________________________|')
    opcion = int(input('->'))
    return opcion

def menu_filtros():
    print('***********************************')
    print('**      AUTOSCLS- Filtros        **')
    print('***********************************')
    print('|                                 |')
    print('|       1. Filtro Exacto          |')
    print('|       2. Filtro Desde           |')
    print('|       3. Filtro Hasta          |')
    print('|       4. Deshacer Filtros       |')
    print('|       5. Reportar               |')
    print('|       6. Salir                  |')
    print('|                                 |')
    print('|       Elija Opcion              |')
    print('|                                 |')
    print('|_________________________________|')
    opcion = int(input('->'))
    return opcion

def menu_estadisticas():
    print('***********************************')
    print('**      AUTOSCLS- Ordenar        **')
    print('***********************************')
    print('|                                 |')
    print('|       1. Autos por año          |')
    print('|       2. Autos por marca        |')
    print('|       3. Marca más cara         |')
    print('|       4. Marca más barata       |')    
    print('|       5. Salir                 |')
    print('|                                 |')
    print('|       Elija Opcion              |')
    print('|                                 |')
    print('|_________________________________|')
    opcion = int(input('->'))
    return opcion


def filtrar_exacto(lista, campo, valor):
    lista_pos = []
    for pos, item in enumerate(lista) :
        if item[campo] == valor :
            lista_pos.append(pos)    
    return lista_pos

def filtrar_desde(lista, campo, valor):
    lista_pos = []
    for pos, item in enumerate(lista) :
        if item[campo] >= valor :
            lista_pos.append(pos)    
    return lista_pos

def filtrar_hasta(lista, campo, valor):
    lista_pos = []
    for pos, item in enumerate(lista) :
        if item[campo] <= valor :
            lista_pos.append(pos)    
    return lista_pos

def autos_por_año(lista):
    dic = {}
    for item in lista:
        if not item['año'] in dic :
            dic[item['año']] = 1
        else :
            dic[item['año']] += 1
    return dic        

def autos_por_marca(lista):
    dic = {}
    for item in lista:
        if not item['marca'] in dic :
            dic[item['marca']] = 1
        else :
            dic[item['marca']] += 1
    return dic
    
def marca_mas_cara(lista):
    mayor_precio = lista[0]['precio']
    marca = lista[0]['marca']
    for item in lista:
        if item['precio'] > mayor_precio:
            mayor_precio = item['precio']
            marca = item['marca']
    return marca 

def marca_mas_barata(lista):
    mayor_precio = lista[0]['precio']
    marca = lista[0]['marca']
    for item in lista:
        if item['precio'] < mayor_precio:
            mayor_precio = item['precio']
            marca = item['marca']
    return marca        

def update(lista, posiciones):
    nueva_lista = []
    for i in posiciones :
        nueva_lista.append(lista[i])
    return nueva_lista
def cast_valor(campo, valor):
    if campo in ['precio'] :
        valor = float(valor)
    if campo in ['km', 'año'] :
        valor = int(valor)
    return valor 
def procesar_filtros(lista): 
    sublista = lista    
    opcion = menu_filtros()
    while opcion != 6 :        
        if opcion == 1 :
            campo = input('campo:')
            valor = input('valor:')
            valor = cast_valor(campo, valor)
            posiciones = filtrar_exacto(sublista, campo, valor)
            sublista  = update(sublista, posiciones)
            reportar(sublista, range(len(sublista)))
        elif opcion == 2 :    
            campo = input('campo:')
            valor = input('valor:')
            valor = cast_valor(campo, valor)
            posiciones = filtrar_desde(sublista, campo, valor)
            sublista  = update(sublista, posiciones)
            reportar(sublista, range(len(sublista)))
        elif opcion == 3 :
            campo = input('campo:')
            valor = input('valor:')
            valor = cast_valor(campo, valor)
            posiciones = filtrar_hasta(sublista, campo, valor)
            sublista  = update(sublista, posiciones)
            reportar(sublista, range(len(sublista)))            
        elif opcion == 4 :            
            sublista = lista                        
            reportar(sublista, range(len(sublista)))
        elif opcion == 5 :
            reportar(sublista, range(len(sublista)))        
          
        opcion = menu_filtros() 

def reportar_estadisticas(dic):
    for k in dic :
        print('{} -> {}'.format(k, dic[k]))

def procesar_estadisticas(lista):     
    opcion = menu_estadisticas()
    while opcion != 5 :        
        if opcion == 1 :
            dic = autos_por_año(lista)     
            reportar_estadisticas(dic)       
        elif opcion == 2 :    
            dic = autos_por_marca(lista)     
            reportar_estadisticas(dic)
        elif opcion == 3 :
            print(marca_mas_cara(lista))            
        elif opcion == 4 :
            print(marca_mas_barata(lista))                      
        opcion = menu_estadisticas()
                
    
if __name__ == '__main__' :
    autos = [
         {'idx': 0, 'marca': 'Kia',  'formato': 'Sedán', 'año': 2020, 'km': 15000, 'precio': 10500000},
         {'idx': 1, 'marca': 'Kia',  'formato': 'Camioneta', 'año': 2015, 'km': 86000, 'precio': 13790000},
         {'idx': 2, 'marca': 'Kia',  'formato': 'City', 'año': 2018, 'km': 79500, 'precio': 9470000},
         {'idx': 3, 'marca': 'Suzuki',  'formato': 'Hatchback', 'año': 2017, 'km': 65000, 'precio': 8990000},
         {'idx': 4, 'marca': 'Suzuki',  'formato': 'Camioneta', 'año': 2010, 'km': 133000, 'precio': 11000000},
         {'idx': 5, 'marca': 'Suzuki',  'formato': 'Hatchback', 'año': 2022, 'km': 5000, 'precio': 14000000},
         {'idx': 6, 'marca': 'Nissan',  'formato': 'Sedán', 'año': 2022, 'km': 5000, 'precio': 19000000},
         {'idx': 7, 'marca': 'Nissan',  'formato': 'Camioneta', 'año': 2026, 'km': 42000, 'precio': 15000000},
         {'idx': 8, 'marca': 'Nissan',  'formato': 'Camioneta', 'año': 2014, 'km': 84000, 'precio': 14000000},
         {'idx': 9, 'marca': 'Toyota',  'formato': 'Camioneta', 'año': 2017, 'km': 61000, 'precio': 18500000},
         {'idx': 10, 'marca': 'Toyota',  'formato': 'Sedán', 'año': 2021, 'km': 12500, 'precio': 21500000}] 
    opcion = menu() 
    while  opcion != 4:        
        if opcion == 1 :
            reportar(autos, range(len(autos)))
        elif opcion == 2 :
            procesar_filtros(autos)
            
        elif opcion == 3 :
            procesar_estadisticas(autos)
        opcion = menu()
    print('FIN')



