N = int(input())
data = []
for i in range(N):
    a,b = map(int,input().split())
    data.append(2-a+b)
for i in data:
    print(i)