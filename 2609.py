a,b = map(int,input().split())
from math import gcd
print(gcd(a,b))
print(int(a*b/gcd(a,b)))