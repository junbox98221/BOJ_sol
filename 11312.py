import sys
for i in range(int(sys.stdin.readline())):
    A,B = map(int,sys.stdin.readline().split())
    print((int(A/B)**2))