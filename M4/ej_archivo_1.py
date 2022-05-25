"""
"""
f = open('comunas.txt','a')
f.write('6. La Reina')    
f.close() 

f = open('comunas.txt')
for linea in f:
    print(linea.strip())
f.close()
