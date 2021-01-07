a,b= 1,1
data = []
while a!=0 or b != 0:
    a,b = map(int,input().split())
    data.append((a,b))

for a,b in data[:-1]:
    if a>b:
        print('Yes')
    else:
        print('No')