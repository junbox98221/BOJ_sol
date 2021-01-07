from math import gcd

case = int(input())
ls = []
for i in range(case):
    a,b = map(int,input().split())
    result = a*b//gcd(a,b)
    ls.append(result)


for i in ls:
    print(i)