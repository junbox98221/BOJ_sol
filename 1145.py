import sys
from math import gcd
from itertools import combinations

data = list(map(int,sys.stdin.readline().split()))
data3 = list(combinations(data,3))
ans = 1000000
for a,b,c in data3:
    temp = a*b*c/gcd(a,b)/gcd(b,c)/gcd(a,c)*gcd(a,b,c)
    if temp < ans:
        ans = temp
print(int(ans))