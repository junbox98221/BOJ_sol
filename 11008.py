import sys

for i in range(int(sys.stdin.readline())):
    s,p = sys.stdin.readline().split()
    time = 0
    n = s.count(p)
    time = n + len(s) - (len(p)*n)
    print(time)