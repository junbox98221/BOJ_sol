q = int(input())

dicc = {}
for i in range(q):
    data = list(map(int,input().split()))
    divide = data[2]%data[0]
    integer = data[2]//data[0]
    if divide == 0:
        dicc[data[0]] = integer
    else:
        dicc[divide] = integer+1


for i,j in dicc.items():
    print('{}{:02d}'.format(i,j))
