from math import *
p = 1 

for n in range(1,17):
    a = n**4 / 4 + n**3 / 3 + n**2 / 2 + n
    b = 3*n**3 + 2*n**2 + n
    c = log10(n + 1)
    p = p* a/b *c

print(p)
