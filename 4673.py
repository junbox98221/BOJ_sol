def cal(a):
    x = 1
    lis = []
    while(x<=a):
        x_str = str(x)
        c = x
        for i in x_str:
            c += int(i)
        lis.append(c)
        x += 1

    ls_10000 = list(set(range(1,a+1)) - set(lis))
    ls_10000.sort()
    for i in ls_10000:
        print(i)

cal(10000)