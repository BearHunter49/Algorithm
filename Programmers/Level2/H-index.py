from bisect import bisect_left


def solution(citations):
    answer = 0
    citations.sort()
    length = len(citations)
    for i in range(length, 0, -1):
        cited_count = length - bisect_left(citations, i)
        if cited_count >= i:
            answer = i
            break

    return answer


print(solution([3, 3, 3, 3, 5]))