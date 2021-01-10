case = int(input())
data = []
for i in range(case):
    ls = input().split()
    a = list(map(lambda x: '0' + x if len(x) < 2 else x, ls[1:]))
    birth = ''.join(reversed(a))
    data.append((ls[0],birth))

data = sorted(data,key = lambda data:data[1])

#lambda 개념 및 다른 사람들 풀이 확인!
print(data[-1][0])
print(data[0][0])