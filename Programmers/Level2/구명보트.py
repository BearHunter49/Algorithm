import heapq


def solution(people, limit):
    answer = 0
    people.sort(reverse=True)

    max_index = 0
    min_index = len(people) - 1
    while True:
        if max_index > min_index:  # 모두 건넘
            break
        if max_index == min_index:  # 1명 남음
            answer += 1
            break

        max_weight = people[max_index]
        min_weight = people[min_index]

        if max_weight + min_weight <= limit:
            answer += 1
            max_index += 1
            min_index -= 1
        else:
            answer += 1
            max_index += 1

    return answer


print(solution([70, 50, 80, 50], 100))  # 3

