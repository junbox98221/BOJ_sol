import sys

N = int(sys.stdin.readline())
M,K = map(int,sys.stdin.readline().split())
data = list(map(int,sys.stdin.readline().split()))
data.sort()

if sum(data) < M * K:
    print('STRESS')
else:
    i = -1
    while(sum(data[i:])<M*K):
        i -= 1
    print(-i)
