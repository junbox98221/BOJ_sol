N = int(input())
data = []
for i in range(N):
    a,b = map(int,input().split())
    data.append((a,b))

for a,b in data:
    print('You get {} piece(s) and your dad gets {} piece(s).'.format(a//b,a%b))