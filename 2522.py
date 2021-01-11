N = int(input())

for i in range(N):
    blank = ' '
    star = '*'
    print('{}{}'.format(blank*(N-i-1),star*(i+1)))
for i in range(N-1):
    blank = ' '
    star = '*'
    print('{}{}'.format(blank*(i+1),star*(N-1-i)))