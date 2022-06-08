"""
"""
def collatz(n, step = 1):
    print('{} {}'.format(step, n))
    if n != 1 :
        if n % 2 == 0 :
            collatz(n/2, step + 1)
        else :
            collatz(3*n + 1, step + 1)
            

collatz(200)