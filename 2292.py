N = int(input())

import math

a = math.ceil((N-1)/6)

x = 0

c = 1
n = 1
while( x < a):
    x += c
    c += 1
    n +=1

print(n)

