input_list = list(map(int, list(input())))

result = 0
for num in input_list:

    if num < 2 or result < 2:  # 0이나 1은 더해주기 or result가 0이면 더하기
        result += num
    else:  # 아니면 곱하기
        result *= num

print(result)

