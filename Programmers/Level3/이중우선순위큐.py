import heapq


def solution(operations):
    answer = []

    checked = dict()
    min_heap = list()
    max_heap = list()

    for operation in operations:
        alphabet, number = operation.split()
        number = int(number)

        if alphabet == "I":  # 삽입
            heapq.heappush(min_heap, number)
            heapq.heappush(max_heap, -number)
            checked[number] = checked.get(number, 0) + 1
        else:
            if number == 1:  # 최댓값
                while max_heap:
                    max_num = heapq.heappop(max_heap) * -1
                    if checked[max_num] == 0:  # 이미 처리함
                        continue

                    checked[max_num] -= 1
                    break

            else:  # 최솟값
                while min_heap:
                    min_num = heapq.heappop(min_heap)
                    if checked[min_num] == 0:  # 이미 처리함
                        continue

                    checked[min_num] -= 1
                    break

    if not min_heap or not max_heap:  # 둘 중 하나라도 비어있으면 다 뽑은 것
        answer = [0, 0]
    else:
        max_num = 0
        min_num = 0
        while max_heap:
            max_num = heapq.heappop(max_heap) * -1
            if checked[max_num] == 0:
                continue
            break

        while min_heap:
            min_num = heapq.heappop(min_heap)
            if checked[min_num] == 0:
                continue
            break
        answer = [max_num, min_num]

    return answer


print(solution(["I 16", "D 1"]))  # [0, 0]
