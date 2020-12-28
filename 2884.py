import re
x = input()

numbers = re.findall("\d+", x)#문자열에서 숫자 추출
h = int(numbers[0])
m = int(numbers[1])

if(m < 45):
    m = m + 60 -45
    if(h == 0):
        h = 23
    else:
        h = h -1
else:
    m = m - 45
answer = str(h) + " " + str(m)
print(answer)