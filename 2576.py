data = []

for i in range(7):
    N = int(input())
    if N % 2!=0:
        data.append(N)
if len(data) == 0:
    print(-1)
else:
    print(sum(data))
    print(min(data))