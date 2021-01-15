import sys
for i in range(int(sys.stdin.readline())):
    M,type = sys.stdin.readline().split()
    data = sys.stdin.readline().split()
    for i in data:
        if type == 'C':
            print(ord(i)-64,end = ' ')
        else:
            print(chr(int(i)+64),end = ' ')

