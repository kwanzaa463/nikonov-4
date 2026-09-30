import math
s = 0

for n in range(1,51):
    s += (2.2**(2*n+1)) / math.factorial(2*n+1)

print(s)
