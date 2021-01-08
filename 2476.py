game = int(input())
data1 = []
for i in range(game):
    data1.append(list(map(int,input().split())))

price = []
for data in data1:

    if len(set(data)) == 3:
        price.append(max(data)*100)
    elif len(set(data)) == 2:
        for i in list(set(data)):
            if data.count(i)==2:
                price.append(1000 + i*100)
    else:
        price.append(10000 + data[0]*1000)

print(max(price))