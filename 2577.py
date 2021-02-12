a = int(input())
b = int(input())
c = int(input())
d = a * b * c
e = list(str(d))
ans = [0 for i in range(10)]
for i in range(0, 10):
    for j in e:
        if str(i) == j:
            ans[i] = ans[i] + 1

for i in ans:
    print(i)
