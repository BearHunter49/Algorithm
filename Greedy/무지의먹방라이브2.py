def solution(food_times, k):
    answer = 0
    size = len(food_times)

    # 시간 내에 처리 가능
    if sum(food_times) <= k:
        return -1

    # 싸이클
    while True:
        min_remain_time = int(1e9)
        remain_food = 0
        for i, time in enumerate(food_times):
            if time > 0:
                remain_food += 1  # 남은 음식 개수

                if time < min_remain_time:  # 최소값 갱신
                    min_remain_time = time

        if min_remain_time * remain_food <= k:  # 싸이클 돌 수 있음
            k -= (min_remain_time * remain_food)
            for i in range(size):  # 남은 시간 갱신
                food_times[i] -= min_remain_time
        else:  # 싸이클 못돔
            remain_count = k % remain_food
            for i, time in enumerate(food_times):
                if time > 0:
                    if remain_count == 0:
                        answer = i + 1
                        break

                    remain_count -= 1
            break

    return answer


print(solution([3, 1, 2], 5))

# heap 이 강제됨!


