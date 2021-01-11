N = int(input())

for i in range(N):
    blank = ' '
    star = '*'
    print('{}{}'.format(blank*(N-i-1),star*(2*i+1)))