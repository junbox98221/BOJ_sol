def bino_search(n,k):
    bs = 0
    br = n**2
    while bs < br:
        bc = (bs+ br)//2
        count = 0

        for i in range(1,n+1):
            if n >= bc//i:
                count += bc//i
            else:
                count += n
        print('bs:%d br:%d count:%d' % (bs, br,count))
        if count < k:
            bs = bc + 1
        else:
            br = bc - 1
    return bs

def main(n,k):
    print(bino_search(n,k))
if __name__ == '__main__':
    n = int(input())
    k = int(input())
    main(n, k)