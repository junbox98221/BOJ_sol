for i in range(int(input())):
    P,M = map(int,input().split())
    data = []
    for j in range(P):
        a = input()
        if a not in data:
            data.append(a)
    print(P - len(data))
