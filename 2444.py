N = int(input())

for i in range(N):
    blank = ' '
    star = '*'
    print('{}{}'.format(blank*i,star*(2*N-1-2*i)))