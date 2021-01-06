count = int(input())
data23 = []

for i in range(count):
    data = list(input().split())
    num = float(data[0])
    for j in data[1:]:
        if j == '@':
            num *= 3
        elif j == '%':
            num += 5
        elif j == '#':
            num -= 7
    data23.append(num)
for num in data23:
    print('{:0.02f}'.format(float(num)))
