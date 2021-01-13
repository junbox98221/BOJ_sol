data1 = []
for i in range(3):
    data1.append(list(input().split()))

for data in data1:
    if data.count('0') == 0:
        print('E')
    if data.count('0') == 1:
        print('A')
    if data.count('0') == 2:
        print('B')
    if data.count('0') == 3:
        print('C')
    if data.count('0') == 4:
        print('D')