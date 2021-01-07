data = list(map(int,input().split()))

if len(set(data)) == 3:
    print(max(data)*100)
elif len(set(data)) == 2:
    for i in list(set(data)):
        if data.count(i)==2:
            print(1000 + i*100)
else:
    print(10000 + data[0]*1000)