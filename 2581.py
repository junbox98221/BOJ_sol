M = int(input())
N = int(input())
data = []
for i in range(M,N+1):
    if i == 1:
        continue
    check = 0
    for j in range(2,i):
        if i % j == 0:
            check = 1
            break
    if check == 0:
        data.append(i)

if len(data) != 0:
    print('%d\n%d' %(sum(data),min(data)))
else:
    print(-1)