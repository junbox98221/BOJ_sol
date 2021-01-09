cook_sec = int(input())

a = cook_sec//300
b = (cook_sec - 300 * a)//60
c = (cook_sec -300 * a - 60 * b)// 10
if list(str(cook_sec))[-1] != '0':
    print(-1)
else:
    print('{0} {1} {2}'.format(a,b,c))
