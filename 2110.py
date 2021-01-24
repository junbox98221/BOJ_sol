import sys

N,C = map(int,sys.stdin.readline().split())
lis = []
for i in range(N):
    lis.append(int(sys.stdin.readline()[:-1]))
lis.sort()

def bin_C(lis,C):
    bs = 0
    br = lis[-1] - lis[0]
    res = 0
    while bs <= br:
        bc = (bs + br) // 2
        start = lis[0]
        check = 1
        for i in lis[1:]:
            if i - start >= bc:
                start = i
                check += 1
        if check >= C:
            res = bc
            bs = bc + 1
        else:
            br = bc - 1
    return res

print(bin_C(lis,C))