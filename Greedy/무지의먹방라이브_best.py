import heapq


def solution(food_times, k):
    answer = 0

    # 시간 내 다 먹을 수 있는 케이스
    total = sum(food_times)
    if total <= k:
        return -1

    # 알고리즘
    heap = list()
    food_count = len(food_times)
    for i in range(food_count):  # 힙에 다 넣기
        heapq.heappush(heap, (food_times[i], i + 1))  # (먹는데 걸리는 시간, 음식 번호)

    previous_time = 0  # 전 까지 먹은 최소 음식 시간
    while True:
        min_time = heap[0][0] - previous_time  # 최소 음식 시간
        time = min_time * food_count

        if time <= k:  # 최소 시간 음식으로 한 바퀴 돌 수 있을 경우
            k -= time
            heapq.heappop(heap)
            food_count -= 1
            previous_time += min_time

        else:  # 못 돌 경우
            heap.sort(key=lambda x: x[1])  # 음식 번호로 오름차순 정렬
            answer = heap[k % food_count][1]
            break

    return answer


user_input = input()
user_input = user_input.replace(' ', '').replace('[', '').replace(']', '')
input_list = user_input.split(',')
food_items = list(map(int, input_list[:-1]))
k = int(input_list[-1])

print(solution(food_items, k))










