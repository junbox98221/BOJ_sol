man = int(input())

count = 0
for i in range(man):
    opinion = input()
    if opinion == '1':
        count += 1
    else:
        count -= 1

if count > 0:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")