data = []
a,b = map(int,input().split())
while a !=0 or b != 0:
    data.append(a+b)
    a,b = map(int,input().split())
for i in data:
    print(i)