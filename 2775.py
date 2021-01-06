t = int(input())

for _ in range(t):
    floor = int(input())
    num = int(input()) #입력받은 floor num 정보 바탕으로 바로 for돌리기
    f0 = [i for i in range(1,num+1)]
    for k in range(floor):
        for i in range(1,num):
            f0[i] += f0[i-1] # 이 부분은 이야..
    print(f0[-1])
