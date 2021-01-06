sugar = int(input())

div3 = sugar//3
div5 = sugar//5

mk3 = 0
mk5 = 0
count = sugar
for i in range(div5+1):
    for j in range(div3+1):
        if sugar == i*5 + j*3:
            temp = i + j
            if count > temp:
                count = temp
if count==sugar:
    print(-1)
else:
    print(count)