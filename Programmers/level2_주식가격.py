def solution(prices):
    answer = []
    length = len(prices)

    for i in range(length):
        pivot = prices[i]
        count = 0
        for j in range(i + 1, length):
            count += 1
            if pivot > prices[j]:
                break

        answer.append(count)
    return answer


print(solution([1, 5, 3, 2, 3]))

