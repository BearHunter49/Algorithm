X = int(input())
dp_list = [0] * 30001

for i in range(2, X + 1):

    # d의 경우
    dp_list[i] = dp_list[i - 1] + 1

    if i % 5 == 0:  # a의 경우
        dp_list[i] = min(dp_list[i], dp_list[i // 5] + 1)
    if i % 3 == 0:  # b의 경우
        dp_list[i] = min(dp_list[i], dp_list[i // 3] + 1)
    if i % 2 == 0:  # c의 경우
        dp_list[i] = min(dp_list[i], dp_list[i // 2] + 1)


print(dp_list[X])







