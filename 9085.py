T = int(input())
data = []
for i in range(T):
    N = int(input())
    data.append(sum(list(map(int,input().split()))))
for j in data:
    print(j)