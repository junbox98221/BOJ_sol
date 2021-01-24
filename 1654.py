import sys
K,N = map(int,sys.stdin.readline().split())
liss = list()
for i in range(K):
    liss.append(int(sys.stdin.readline()))

def bin_search(lis,N):
    bs = 1
    br = max(lis)
    ans = 0
    while True:
        bc = (bs+br)//2
        temp = 0
        for i in lis:
            temp += i // bc
        if temp < N:
            br = bc - 1
        elif temp >= N and bc < br:
            ans = bc
            bs = bc + 1
        elif temp < N and bc == br:
            return ans
        else:
            return bc

print(bin_search(liss,N))