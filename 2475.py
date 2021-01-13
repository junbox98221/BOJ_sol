data = list(map(int,input().split()))

a = list(x**2 for x in data)
print(sum(a)%10)