case = int(input())
data = []
for i in range(case):
    a,b = input().split()
    data.append(int(a)+int(b))
for i in range(case):
    print(data[i])