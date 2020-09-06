test_list = [7, 0, 5, 5, 4, 9, 7, 3, 2, 1, 8]

max_num = max(test_list)
min_num = min(test_list)
length = len(test_list)

counting_sort = [0] * (max_num - min_num + 1)

for num in test_list:
    counting_sort[num] += 1

result = list()
for index, count in enumerate(counting_sort):
    for _ in range(count):
        result.append(index)

print(result)
