"""
"""

def mi_funcion_global() :
    print(x)
    
def mi_funcion(x):    
    x= x + 1    
    return x


x = 10 
y = 5
z = mi_funcion(y)
print(x)
print(y)
print(z)

mi_funcion_global()
print(x)