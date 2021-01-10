N = int(input())

for i in range(1,N+1):
    a = '*'*(N+1-i)
    print(' '*(i-1),end = '')
    print(a)