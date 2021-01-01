import re

count = int(input())

for i in range(1,count+1):
    z = input()
    numbers = re.findall("\d+", z)  # 문자열에서 숫자 추출
    x = numbers[0]
    y = numbers[1]
    z = int(x)+int(y)
    print("Case #"+str(i)+": "+x+" + "+y+" = "+str(z))

