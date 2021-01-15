import sys
from itertools import combinations
data = list()
while True:
    dat = list(map(int,sys.stdin.readline().split()))
    if dat == [0]:
        break
    data.append(dat[1:])
for i in data:
    j = list(combinations(i,6))
    for k in j:
        print('{} {} {} {} {} {}'.format(*k))
    print()
