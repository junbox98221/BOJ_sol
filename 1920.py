N = int(input())
ls = sorted((map(int,input().split())))
M = int(input())
ls2 = list(map(int,input().split()))

def bin_search(a,key):
    bl = 0
    br = len(a) - 1
    count = 0
    while bl <= br:
        bc = (bl+br)//2
        if a[bc] > key:
            br = bc - 1
        elif a[bc] < key:
            bl = bc + 1
        else:
            count = 1
            break
    print(count)

for i in ls2:
    bin_search(ls,i)