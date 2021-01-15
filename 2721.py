import sys
for i in range(int(sys.stdin.readline())):
    ans1 = 0
    for j in range(1 ,1+int(sys.stdin.readline())):
        ans1 += int(j * ((j+1)*(j+2)/2))
    print(ans1)