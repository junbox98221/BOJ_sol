x = input()
countt = 0
x_len = len(x)

y = list(x)
Croatia = ['c=','c-','dz=','d-','lj','nj','s=','z=']

for i in Croatia:
    while i in x:
        countt += 1
        x_len = x_len - len(i)
        index = x.index(i)
        lenn = len(i)
        x = x[:index] +' '+ x[index+lenn-1:]


print(countt+x_len)



