def solution(d, budget):
    answer = 0

    d.sort()
    total = 0
    for price in d:
        total += price
        if total > budget:
            break
        answer += 1

    return answer


print(solution([1,3,2,5,4], 9))  # 3
