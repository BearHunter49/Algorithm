def find_next_max(arr, index_arr):
    max_num = -1
    max_index = -1

    for i, num in enumerate(arr):
        if i in index_arr:
            continue

        if num > max_num:
            max_num = num
            max_index = i

    return max_num, max_index


def solution(land):
    answer = 0

    row = len(land)
    check_list = [[-1, -1] for _ in range(row)]  # [최대값, 인덱스]

    each_row_max = list()
    for i, now_land in enumerate(land):
        max_num = max(now_land)
        max_index = now_land.index(max_num)

        each_row_max.append([max_num, max_index, i])  # [최대값, 인덱스, row]

    each_row_max.sort(reverse=True, key=lambda x: x[0])

    for num, index, r in each_row_max:
        pre_row = r - 1
        next_row = r + 1
        check_row = -1

        if pre_row < 0:  # 인덱스 0
            check_row = next_row
        elif next_row >= row:  # 인덱스 row
            check_row = pre_row

        if check_row != -1:
            if check_list[check_row][1] == index:  # 인덱스 겹침
                next_max_num, next_max_index = find_next_max(land[r], [index])
                check_list[r] = [next_max_num, next_max_index]

            else:  # 안겹침
                check_list[r] = [num, index]

        else:
            pre_index = check_list[pre_row][1]
            next_index = check_list[next_row][1]

            if index in [pre_index, next_index]:  # 인덱스 겹침
                next_max_num, next_max_index = find_next_max(land[r], [pre_index, next_index])
                check_list[r] = [next_max_num, next_max_index]

            else:  # 안겹침
                check_list[r] = [num, index]

    for info in check_list:
        answer += info[0]

    return answer


print(solution([[1,2,3,4],[5,6,7,8],[9,9,9,15], [1,1,1,25]]))
