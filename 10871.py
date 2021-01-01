import re

x = input()
y = input()

num = re.findall("\d+",x)
lis = re.findall("\d+",y)
a = ""
compare = int(num[1])
for i in lis:
    if(int(i)< compare):
        a = a + i +" "

print(a)