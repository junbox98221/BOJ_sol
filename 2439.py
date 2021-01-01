num = int(input())

for i in range(0,num):
    space = " "*(num-i-1)
    print(space+"*"*(i+1))