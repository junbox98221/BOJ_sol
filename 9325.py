case = int(input())
price = [0 for i in range(case)]
for i in range(case):
    price[i] += int(input())
    j = int(input())
    for k in range(j):
        a,b = map(int,input().split())
        price[i] += a*b
for i  in price:
    print(i)