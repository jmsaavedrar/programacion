fa = open('archivoA.txt')
fb = open('archivoB.txt')
fc = open('archivoC.txt', 'w')

lineaA = fa.readline().strip()
lineaB = fb.readline().strip()

while len(lineaA)>0 and len(lineaB)>0 :
    if lineaA < lineaB :
        fc.write(lineaA + '\n')
        lineaA = fa.readline().strip()
    else :
        fc.write(lineaB + '\n')
        lineaB = fb.readline().strip()
        
while len(lineaA)>0  :
    fc.write(lineaA + '\n')
    lineaA = fa.readline().strip()
    
while len(lineaB)>0  :
    fc.write(lineaB)
    lineaB = fb.readline().strip()
    
fa.close()
fb.close()
fc.close()

f = open('archivoC.txt')
for linea in f :
    print(linea.strip())
f.close()