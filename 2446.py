N = int(input())
star = '*'
blank = ' '
for i in range(N):
    print('{}{}'.format(blank*(i),star*(2*N-1-2*i)))
for i in range(N-1):
    print('{}{}'.format(blank*(N-2-i),star*(2*i)+star*3))