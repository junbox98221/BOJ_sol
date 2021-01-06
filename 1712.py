data = list(map(int,input().split()))

d0,d1,d2 = data

if d1 >= d2:
    print(-1)

else:
    sale_num = d0//(d2 - d1)
    print(sale_num + 1)


