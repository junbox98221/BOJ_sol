N = int(input())

for i in range(N):
    blank = ' '
    star = '*'
    print('{}'.format(star*(i+1)))
for i in range(N-1):
    blank = ' '
    star = '*'
    print('{}'.format(star*(N-i-1)))