x = input()
j = []
for i in range(int(x)):
    j.append(input())

for i in j:
    score = 0
    j = 0
    for k in enumerate(i):
        if(k[1] == 'O'):
            j += 1
            score += j
        else:
            j = 0
    print(score)