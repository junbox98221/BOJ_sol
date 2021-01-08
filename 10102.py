check = int(input())

ls = list(input())

if ls.count(ls[0]) > len(ls)/2:
    print(ls[0])
elif ls.count(ls[0]) == len(ls)/2:
    print('Tie')
else:
    if ls[0]=='A':
        print('B')
    else:
        print('A')