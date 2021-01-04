count = int(input())

zero = 0
for i in range(count):
    word = input()
    word_to_list = list(word)
    word_to_set = []
    for m in word_to_list:
        if m not in word_to_set:
            word_to_set.append(m)
    for j in word_to_set:
        alp_count = word.count(j)
        if  [j for k in range(alp_count)] != word_to_list[0:alp_count]:
            break
        elif alp_count == len(word_to_list):
            zero += 1
        else:
            word_to_list = word_to_list[alp_count:]

print(zero)


