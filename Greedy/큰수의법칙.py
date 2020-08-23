N, M, K = map(int, input().split())
input_list = list(map(int, input().split()))

max_num = max(input_list)
max_count = input_list.count(max_num)
result = 0

if max_count == 1:  # 큰 수가 1
    max_index = input_list.index(max_num)
    del input_list[max_index]
    sec_max_num = max(input_list)

    # 2번째 큰 수를 포함하여 계산하기
    q = M // (K + 1)
    r = M % (K + 1)

    if r == 0:  # 나머지 없을 경우
        result = (max_num * K) * q + (sec_max_num * 1) * q
    else:  # 나머지 있을 경우
        result = (max_num * K) * q + (sec_max_num * 1) * q + (max_num * r)

else:  # 큰 수가 2개 이상
    result = max_num * M

print(result)

