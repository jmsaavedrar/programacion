"""

dict =  {rank: int, 
        tipo:string, 
        platform: string, 
        year: int, 
        genre: string, 
        publisher: string, 
        US_sales: float, 
        JP_sales:float, 
        Other_sales_ float, 
        global_sales: float } "
"""

import matplotlib.pyplot as plt

def leer_archivo(filename):
    datos_dic = []
    f = open(filename)
    datos = [linea.strip().split(',') for linea in f]
    for item in datos[1:] :         
        datos_dic.append({'rank': int(item[0]),
                            'tipo': item[1],
                            'platform': item[2],
                            'year': int(item[3]),
                            'genre' : item[4],
                            'publisher' : item[5],
                            'US_sales': float(item[6]),
                            'JP_sales': float(item[7]),
                            'Other_sales': float(item[8]),
                            'Global_sales': float(item[9])                        
                            })
    return datos_dic

def contar_instancias(datos, campo):
    dic = {}
    for item in datos:
        if not item[campo] in dic :
            dic[item[campo]] = 1
        else :
            dic[item[campo]] += 1
    return dic    

                     
    
def grafico1(datos):
    #ordenar(datos, 'year')
    dic = contar_instancias(datos, 'year')
    years =sorted(dic)                    
    conteo = [dic[year] for year in years]    
    plt.plot(years, conteo)    
    

if __name__ == '__main__' :
    filename = '/home/jsaavedr/Downloads/vgsales.csv'
    dic = leer_archivo(filename)
    grafico1(dic)
    plt.show()