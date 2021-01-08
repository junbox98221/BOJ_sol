location_x = []
location_y = []
for i in range(3):
    x,y = map(int,input().split())
    location_x.append(x)
    location_y.append(y)
x_ans = 0
for x in list(set(location_x)):
    if location_x.count(x) == 1:
        x_ans = x
y_ans = 0
for y in list(set(location_y)):
    if location_y.count(y) == 1:
        y_ans = y
print(x_ans,y_ans)