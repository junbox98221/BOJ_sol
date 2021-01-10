N = int(input())

a = 1
temp = 1
if N == 0:
    print(0)
elif N == 1:
    print(1)
else:
    for i in range(N-2):
        temp1 = a
        a = temp + a
        temp = temp1
    print(a)
