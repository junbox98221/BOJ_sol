data = []
a,b = map(int,input().split())
while a !=0 or b != 0:
    data.append((a, b))
    a,b = map(int,input().split())

for a,b in data:
    if b%a == 0:
        print('factor')
    elif a%b == 0:
        print('multiple')
    else:
        print('neither')