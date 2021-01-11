T = int(input())
data = []
for i in range(T):
    ans = []
    N = int(input())
    data1 = []
    for j in range(N):
        a, b = (map(float, input().split()))
        data1.append((a,b))

    sum = 0
    C_sum = 0
    for C, G in data1:
        C_sum += C*G
        sum += C
    data.append((C_sum,sum))
for C_sum,sum in data:
    if sum !=0:
        print('{} {:.1f}'.format(int(sum),C_sum/sum))
    else:
        print('{} {:.1f}'.format(int(sum),0))
