N = int(input())
a = N
for i in range(1,N):
    N = N*(a-i)
if N == 0:
    print(1)
else:
    print(N)