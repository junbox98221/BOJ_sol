import sys
max = 0
now = 0
for i in range(10):
    p_out,p_in = map(int,sys.stdin.readline().split())
    now = now + p_in - p_out
    if max < now:
        max = now

print(max)