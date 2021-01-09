case = int(input())

data = {'Q1':0,'Q2':0,'Q3':0,'Q4':0,'AXIS':0}
for i in range(case):
    a,b = map(int,input().split())
    if a== 0 or b ==0:
        data['AXIS'] += 1
    elif a >0 and  b>0:
        data['Q1']+= 1
    elif a <0 and b>0:
        data['Q2'] += 1
    elif a <0 and b<0:
        data['Q3'] += 1
    else:
        data['Q4'] += 1

def math_info(AXIS,Q1,Q2,Q3,Q4):
    print('Q1:',Q1)
    print('Q2:', Q2)
    print('Q3:', Q3)
    print('Q4:', Q4)
    print('AXIS:', AXIS)

math_info(**data)

