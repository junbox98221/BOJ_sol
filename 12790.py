import sys
for i in range(int(sys.stdin.readline())):
    HP,MP,AT,DF,Hc,Mc,Ac,Dc = map(int,sys.stdin.readline().split())
    if HP + Hc < 1:
        H = 1
    else:
        H = HP + Hc
    if MP + Mc < 1:
        M = 1
    else:
        M = MP + Mc
    if AT + Ac < 0:
        A = 0
    else:
        A = AT + Ac
    print(H + 5 * M + 2 * A + 2 * (DF + Dc))