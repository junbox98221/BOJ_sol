a = input()
b = input()
cnt = 0
while True:
    if b in a:
        a = a[:a.index(b)]+a[a.index(b)+len(b):]
        cnt += 1
    else:
        break
print(cnt)