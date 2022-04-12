"""
Arábigos a romanos
"""


u = ['','I','II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
d = ['','X','XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
c = ['','C','CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'CM', 'CM']
m = ['', 'M', 'MM', 'MMM']

rom = [u,d, c, m]
numero = int(input('ingrese un número <= 3000 :'))

aux = numero
romanos = ''
it = 0;
while aux != 0:
    r = aux % 10
    aux = aux // 10
    """
    if it == 0 :
        rom = u[r]
    if it == 1 :
        rom = d[r]
    if it == 2 :
        rom = c[r]
    if it == 3 :
        rom = m[r]
    """
    romanos = rom[it][r] + romanos
    it = it + 1   
print(romanos)

     


