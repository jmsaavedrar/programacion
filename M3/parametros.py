"""
"""

def funcion(x):
    x = x + 1    
    return x 

def funcion_2(x):
    x.append(1)
    
def funcion_3(x):
    x = [1]

x = 5
y = funcion(x)
print(x)

l = []
funcion_3(l)
print(l)