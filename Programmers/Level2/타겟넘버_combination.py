from itertools import combinations


def solution(numbers, target):
    answer = 0

    length = len(numbers)
    for i in range(length):
        possibles = list(combinations(numbers, i + 1))
        for possible in possibles:

            total = sum(numbers)
            for num in possible:
                total -= (num * 2)
            if total == target:
                answer += 1
        
    return answer


print(solution([1, 1, 1, 1, 1], 3))  # 5







