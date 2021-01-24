import sys

N,M = map(int,sys.stdin.readline().split())
lis = list(map(int,sys.stdin.readline().split()))

def bin_tree(lis,tree_heigh):
    bs = 0
    br = sum(lis)
    temp = 0
    while True:
        bc = (bs+br)//2
        target = 0
        for i in lis:
            if i > bc:
                target += i - bc
        if target < tree_heigh:
            br = bc - 1
        elif target >= tree_heigh and bc < br:
            temp = bc
            bs = bc + 1
        elif temp < bc:
            return bc
        else:
            return temp

print(bin_tree(lis,M))