dish_order = list(input())

last = dish_order[0]
sum = 0
for i in dish_order:
    if last != i:
       sum += 10
    else:
        sum += 5
    last = i

print(sum+5)