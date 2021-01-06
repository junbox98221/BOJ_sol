data = list(map(int,input().split()))

diff = data[0] - data[1]

import math

if math.floor((data[2] - data[0])/diff) == (data[2] - data[0])/diff:
    print(int((data[2] - data[0])/diff + 1))
else:
    print(int(math.floor((data[2] - data[0])/diff) + 2))
