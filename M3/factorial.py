"""
"""

def factorial(x):
    f = 1
    while x > 0 :
        f = f * x
        x = x -1
    return f


for x in range(10) :
    print('factorial de {} es {}'.format(x, factorial(x))) 