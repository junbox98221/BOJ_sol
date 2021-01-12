data = []
N = int(input())
a = 1
for i in range(N):
    b = int(input())
    if i == 0:
        a =b
    else:
        a = a-1+b
print(a)