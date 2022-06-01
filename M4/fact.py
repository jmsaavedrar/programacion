"""
"""

def fact(n):
    if n==1 :
        return 1
    else :
        return n*fact(n-1)

def fib(n):
    if n == 1 or n == 0 :
        return n
    else :
        return fib(n-1) + fib(n-2)
        
    

print(fact(5))
for i in range(20) :
    print(fib(i))