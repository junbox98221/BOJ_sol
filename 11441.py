import sys
N = int(sys.stdin.readline())
l = list(map(int,sys.stdin.readline().split()))
ans = [0] * (N+1)
#주어진 배열의 i,j까지의 합을 구하기 위한 배열을 미리 생성해서
#시간 단축.
for i in range(1,N+1):
    ans[i] = ans[i-1]+l[i-1]

for i in range(int(sys.stdin.readline())):
    a,b=map(int,sys.stdin.readline().split())
    res = ans[b] - ans[a-1]
    sys.stdout.write(str(res) + '\n')
