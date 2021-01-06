put = int(input())


c = 1
count = 0

while put > 0:
    put -= c
    c += 1
    count += 1

if count % 2 != 0:
    print('{0}/{1}'.format(1 -put,count + put))
else:
    print('{0}/{1}'.format(count + put,1 -put))
