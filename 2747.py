N = int(input())

if N == 0:
    print(0)
elif N== 1:
    print(1)
else:
    data = [0,1]
    for i in range(N-1):
        s = data[0]+data[1]
        data = [data[1],s]
    print(s)