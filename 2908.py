qq = list(input().split())
x = list(map(str,qq))

y = []
for i in x:
    a = ""
    for j in i:
        a = j + a
    y.append(a)

if int(y[0]) > int(y[1]):
    print(y[0])
else:
    print(y[1])

