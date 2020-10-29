import math
from itertools import combinations


def solution(nums):
    answer = 0

    # 에라토스테네스의 체
    prime_numbers = [True] * 3001  # 1000까지 3개니 3000까지 가능
    prime_numbers[0] = False
    prime_numbers[1] = False

    for i in range(2, int(math.sqrt(3001)) + 1):
        if not prime_numbers[i]:
            continue

        for j in range(i * 2, 3001, i):
            prime_numbers[j] = False

    possibles = list(combinations(nums, 3))
    for possible in possibles:
        temp_sum = sum(possible)
        if prime_numbers[temp_sum]:
            answer += 1

    return answer


print(solution([1,2,3,4]))  # 1

