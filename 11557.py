case = int(input())
ls = []
for i in range(case):
    school_num = int(input())
    beer_0 = 0
    sc_name_0 = ''
    for j in range(school_num):
        sc_name,beer = input().split()
        if beer_0 < int(beer):
            sc_name_0 = sc_name
            beer_0 = int(beer)
    ls.append(sc_name_0)
for i in  ls:
    print(i)