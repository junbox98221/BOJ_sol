import re
c = []
def sss():
    global c
    while(True):
        x =input()
        num = re.findall("\d+",x)
        a,b = num[0],num[1]
        if(a == '0' and b == '0'):
            break
        c.append(int(a) + int(b))

sss()

for i in c:
    print(i)