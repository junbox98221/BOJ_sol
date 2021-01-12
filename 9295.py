N = int(input())
data = []
for i in range(N):
    data.append((map(int,input().split())))

case = 0

for a,b in data:
    print('Case {}: {}'.format(case+1,a+b))
    case += 1