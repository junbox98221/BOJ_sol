N = int(input())

star = '*'
blank = ' '
for i  in range(N):
    print('{}{}{}'.format(star*(i+1),
                          blank*(2*N-(i+1)*2),star*(i+1)))
for i  in range(N-1):
    print('{}{}{}'.format(star*(N-1-i),
                          blank*(2*i+2),star*(N-1-i)))