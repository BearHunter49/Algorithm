def solution(food_times, k):
    answer = 0

    # 시간 내 다 먹을 수 있는 케이스
    total = sum(food_times)
    if total <= k:
        return -1

    # 알고리즘
    now_min = 0  # 초기값 0
    while True:
        next_min = int(1e9)
        next_not_zero = 0

        for i in range(len(food_times)):
            # 최소값 빼주기
            if food_times[i] != 0:
                food_times[i] -= now_min

            # 시간 빼고 난 후
            if food_times[i] != 0:
                next_not_zero += 1  # 0이 아닌 개수

                if next_min > food_times[i]:  # 최소값 찾기
                    next_min = food_times[i]

        # 싸이클 끝
        if k < next_not_zero:
            break

        # 다음 k 값 연산
        t = next_min * next_not_zero  # 다음에 빼질 k 값

        if k < t:  # 다음에 빼질 값보다 k가 작으면
            now_min = k // next_not_zero
            k -= now_min * next_not_zero
        else:
            now_min = next_min
            k -= t

    for i in range(len(food_times)):
        if food_times[i] != 0:
            if k == 0:
                answer = i
                break
            else:
                k -= 1

    return answer + 1


user_input = input()
user_input = user_input.replace(' ', '').replace('[', '').replace(']', '')
input_list = user_input.split(',')
food_items = list(map(int, input_list[:-1]))
k = int(input_list[-1])

print(solution(food_items, k))

