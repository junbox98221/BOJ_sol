N = int(input())

data = list(map(int,input().split()))
score = 0
check = 1
for i in range(N):
    if data[i] == 1:
        score += check
        check += 1
    else:
        check = 1
print(score)
