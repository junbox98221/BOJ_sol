M = int(input())
N = int(input())

import math
sum = 0

if int(math.sqrt(M)) == math.sqrt(M):
    M = int(math.sqrt(M))
else:
    M = int(math.sqrt(M)) + 1

N = int(math.sqrt(N))
if N - M <1:
    print(-1)
else:
    last = M**2
    for i in range(M,N+1):
        sum += i**2
    print('{}\n{}'.format(sum,last))