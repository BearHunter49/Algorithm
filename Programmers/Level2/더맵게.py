import heapq


def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)

    while True:
        if scoville[0] >= K:  # 모두 K 이상
            break

        if len(scoville) < 2:  # 만들 수 없음
            answer = -1
            break

        lowest = heapq.heappop(scoville)
        second_lowest = heapq.heappop(scoville)

        new_scoville = lowest + (second_lowest * 2)
        heapq.heappush(scoville, new_scoville)
        answer += 1

    return answer


print(solution([1, 2, 3, 9, 10, 12], 7))  # 2
