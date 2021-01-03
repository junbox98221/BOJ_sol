t = int(input())
a = []
for i in range(t):
    num, s = input().split()
    text = ''
    for i in s:
        text += int(num) * i
    a.append(text)

for i in a:
    print(i)