count = int(input())
sc_c = 100
sc_s = 100

for i in range(count):
    a, b = map(int, input().split())
    if a<b:
        sc_c -= b
    elif a>b:
        sc_s -= a
print('{}\n{}'.format(sc_c,sc_s))