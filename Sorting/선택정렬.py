test_list = [7, 0, 5, 4, 9, 3, 2, 1, 8]
length = len(test_list)

for i in range(length):
    min_index = i
    for j in range(i + 1, length):
        if test_list[min_index] > test_list[j]:  # 새로운게 더 작으면
            min_index = j

    test_list[i], test_list[min_index] = test_list[min_index], test_list[i]

print(test_list)