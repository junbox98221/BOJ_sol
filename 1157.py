a = input().upper()
b = list(set(a))
countt = []

for i in b:
    countt.append(a.count(i))

if countt.count(max(countt))>1:
    print('?')
else:
    max_index = countt.index(max(countt))
    print(b[max_index])

