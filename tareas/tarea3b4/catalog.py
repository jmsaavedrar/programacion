"""

"""

import csv 
def read_catalog() :
    f = open('ecommerce.csv')    
    datalist = [item for item in f]
    data = []
    for item in datalist[1:]:
        l = item.strip().split(',')        
        data.append({'id' : l[0],  
         'precio_max' : float(l[1]),
         'precio_min' : float(l[2]),
         'vendedor' : l[3],
         'marca' : l[4],
         'descripcion' : l[5],
         'peso': l[6]})                   
    return data
    
if __name__ == '__main__' :
    data = read_catalog()
    for item in data :
        print(item)
    
        
    


