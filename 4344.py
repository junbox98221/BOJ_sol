x  = int(input())
arr = []
for i in range(x):
    z = list(map(int, list(input().split())))
    arr.append(z[1:])


for j in arr:
    av = sum(j)/len(j)
    a = 0
    for k in j:
        if av<k:
            a+=1
    print(str('%.3f' % (a/len(j)*100))+'%')