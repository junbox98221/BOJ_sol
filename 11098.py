case = int(input())
data = {}
for i in range(case):
    num = int(input())
    price = 0
    name = ''
    for j in range(num):
        price_temp,name_temp = input().split()
        if price < int(price_temp):
            price = int(price_temp)
            name = name_temp
    data[name] = price

for name in data.keys():
    print(name)
