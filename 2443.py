N = int(input())


for i in range(N):
    blank = ' '
    star = '*'
    print('{}{}'.format(blank*(N-i-1),star*(2*i+1)))
for i in range(N-1):
    blank = ' '
    star = '*'
    print(' {}{}'.format(blank*i,star*(2*N-3-2*i)))