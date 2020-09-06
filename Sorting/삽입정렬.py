test_list = [7, 0, 5, 4, 9, 3, 2, 1, 8]
length = len(test_list)

for i in range(1, length):
    for j in range(i, 0, -1):
        if test_list[j] < test_list[j - 1]:  # 바꿔야 하면
            test_list[j], test_list[j - 1] = test_list[j - 1], test_list[j]
        else:
            break

print(test_list)
