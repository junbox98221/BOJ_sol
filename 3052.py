lis = [0 for i in range(10)]
for i in range(10):
    lis[i] = int(input())
b = []
for i in lis:
    a = i%42
    if a not in b:
        b.append(a)
print(len(b))