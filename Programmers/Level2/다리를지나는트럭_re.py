from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0

    wait_trucks = deque(truck_weights)
    on_trucks = deque()
    on_weight = 0
    while wait_trucks:
        next_truck = wait_trucks[0]

        # 1초 지남
        answer += 1
        is_passed = 0
        for i in range(len(on_trucks)):
            on_trucks[i][1] -= 1
            if on_trucks[i][1] == 0:
                is_passed = 1

        if is_passed == 1:  # 하나 건넘
            on_weight -= on_trucks[0][0]
            on_trucks.popleft()

        if on_weight + next_truck > weight:  # 다리 무게 초과
            s = on_trucks[0][1]  # 빠르게 진행시키기
            for i in range(len(on_trucks)):
                on_trucks[i][1] -= s - 1
            answer += s - 1
        else:
            # 다리에 트럭 추가
            on_trucks.append([next_truck, bridge_length])  # (truck 무게, 건너야할 다리 길이)
            on_weight += next_truck
            wait_trucks.popleft()

    # 마지막 트럭 처리
    answer += on_trucks[-1][1]

    return answer


print(solution(2, 10, [7, 4, 5, 6]))  # 8
