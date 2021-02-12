a = input()
b = list(map(int, input().split()))

c = max(b)

for i in b:
    b[b.index(i)] = i / c * 100

print(sum(b) / len(b))
