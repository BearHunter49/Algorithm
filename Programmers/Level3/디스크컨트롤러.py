import heapq
from collections import deque


def solution(jobs):
    answer = 0
    total_num = len(jobs)
    jobs.sort(key=lambda x: x[0])  # 들어온 시간 순으로 정렬

    queue = deque(jobs)  # 대기 큐
    requested_heap = list()  # 실행 요청 우선순위 큐

    time = 0
    while queue or requested_heap:
        # 현재 시간 기준, 입력 요청 순서대로 heap에 넣기
        while queue:
            enter, burst = queue[0]
            if enter <= time:
                queue.popleft()
                heapq.heappush(requested_heap, [burst, enter])  # [실행 시간, 요청 시간]. 실행 시간 기준으로 min heap
            else:
                break

        # 현재 시간 기준 요청이 없음
        if queue and not requested_heap:
            time += 1
            continue

        burst, enter = heapq.heappop(requested_heap)
        time += burst  # 실행
        answer += time - enter  # 요청부터 종료까지

    answer = answer // total_num
    return answer


print(solution([[0, 3], [1, 9], [2, 6]]))  # 9
