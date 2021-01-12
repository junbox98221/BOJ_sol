N = int(input())

data = list(map(int,input().split()))
ans = 0
for i in data:
    if i == 1:
        ans += 1
        continue
    for j in range(2,i):
        if i % j == 0:
            ans += 1
            break
print(N - ans)