case = int(input())

data = []
for j in range(case):
    Y, K = 0, 0
    for i in range(9):
        a,b = map(int,input().split())
        Y += a
        K += b
    data.append([Y,K])

for Y,K in data:
    if Y > K:
        print('Yonsei')
    elif Y<K:
        print("Korea")
    else:
        print('Draw')
