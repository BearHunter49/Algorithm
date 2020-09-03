def solution(food_times, k):
    answer = 0

    total = sum(food_times)
    if total <= k:  # 시간 내 다 먹을 수 있는 케이스
        return -1

    now = 0
    count = 0
    while True:
        if food_times[now] != 0:
            food_times[now] -= 1
            count += 1

        # 회전
        now += 1
        if now == len(food_times):
            now = 0

        if count == k and food_times[now] != 0:
            break

    answer = now + 1

    return answer


user_input = input()
user_input = user_input.replace(' ', '').replace('[', '').replace(']', '')
input_list = user_input.split(',')
food_items = list(map(int, input_list[:-1]))
k = int(input_list[-1])

print(solution(food_items, k))

# 정확성 통과, 시간 초과
