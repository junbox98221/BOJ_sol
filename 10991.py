N = int(input())

star = '* '
blank = ' '

for i in range(N):

    print(blank * (N - 1 - i) + star * (i + 1))
