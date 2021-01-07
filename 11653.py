x = int(input())

i = 2

if x == 1:
    pass
else:
    while x != 1:
        if x % i == 0:
            print(i)
            x = x/i
        else:
            i += 1