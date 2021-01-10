lis = []
for i in range(10):
    a = int(input())
    lis.append(a)

for i in range(9):

    lis[0] = lis[0] - lis[i+1]

print(lis[0])