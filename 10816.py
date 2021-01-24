N = int(input())
pack = sorted(list(map(int,input().split())))
M = int(input())
check = list(map(int,input().split()))
a = max(check) + 1
ans = list()

def bin_search(liss,key):
    bs = 0
    br = len(liss) - 1
    key_count = 0
    lis = liss
    while True:
        bc = (bs+br)//2
        if lis[bc] == key:
            key_count += 1
            del lis[bc]
            lis.append(a)
        elif lis[bc] > key:
            br = bc - 1
        else:
            bs = bc + 1
        if bs > br:
            return key_count

for i in check:
    ans.append(str(bin_search(pack,i)))

print(' '.join(ans))