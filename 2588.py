x = int(input())
y = int(input())
num = []
for i in str(y): #정수를 입력받아서 각 자리수별로 쪼개기 위해
    # 정수형으로 바꾸고 for문으로 반복시켜 배열에 넣고 다시 형 변환해 사용
    num.append(i)
y = 0
j = 0
for i in reversed(num):
    print(x * int(i))
    y = y + x * int(i) * 10 ** j
    j += 1
print(y)



