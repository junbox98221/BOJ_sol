case = int(input())
data = []
for i in range(case):
    no_profit,profit,cost = map(int,input().split())

    if profit - no_profit > cost:
        data.append('advertise')
    elif profit - no_profit == cost:
        data.append('does not matter')
    else:
        data.append('do not advertise')

for i in data:
    print(i)

