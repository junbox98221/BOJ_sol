a = list(map(ord,input()))

ls = [-1 for i in range(97,123)]

for i in a:
    ls[i - 97] = a.index(i)
s = ""
for i in ls:
    s += str(i)+' '

print(s)