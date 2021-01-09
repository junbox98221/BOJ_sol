
data = []
while 1:
    n = int(input())
    if n == -1:
        break
    ls = []
    for i in range(1,n//2+1):
        if n%i == 0:
            ls.append(i)
    ls.append(n)
    data.append(ls)
for ls in data:
    if sum(ls[:-1]) == ls[-1]:
        print('{0} = 1 '.format(ls[-1]),end= '')
        for j in ls[1:-1]:
            print('+ {0} '.format(j),end = '')
        print()
    else:
        print('{0} is NOT perfect.'.format(ls[-1]))

