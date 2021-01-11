N = int(input())
data = []
for i in range(N):
    data.append((map(int,input().split())))

last_apple = 0

for i,j in data:
    last_apple += j - j//i * i
print(last_apple)