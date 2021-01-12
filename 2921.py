N = [i for i in range(int(input())+1)]
ans = 0
for i in range(len(N)):
    ans += (len(N)-i)*i + sum(N[i:])
print(ans)