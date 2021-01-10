now_t = input().split(':')
mission_t= input().split(':')
t = []
#int('01')은 1로 변환된다는 점!
t.append(int(now_t[0])* 3600 + int(now_t[1])*60 + int(now_t[2]))
t.append(int(mission_t[0])* 3600 + int(mission_t[1])*60 + int(mission_t[2]))
ans = 0

if t[0]<t[1]:
    ans = t[1] - t[0]
else:
    ans = 24*60*60 - t[0] + t[1]

# // 와 %는 int형 반환한다는 점
a = ans//3600
b = (ans-a*3600)//60
c = (ans -b*60 -a*3600)%60
print('{0:02d}:{1:02d}:{2:02d}'.format(a,b,c))



