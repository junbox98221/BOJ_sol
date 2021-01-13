data = []
for i in range(4):
    p_out,p_in = map(int,input().split())
    if i == 0:
        data.append(p_in - p_out)
    else:
        data.append(data[i-1] + p_in - p_out)

print(max(data))
