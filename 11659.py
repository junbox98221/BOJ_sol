import sys
N,M = map(int,sys.stdin.readline().split())
data = list(map(int,sys.stdin.readline().split()))
temp = [0]*(N+1)
for i in range(1,N+1):
    temp[i] = temp[i-1]+data[i-1]
for i in range(M):
    a,b = map(int,sys.stdin.readline().split())
    print(temp[b]-temp[a-1])
