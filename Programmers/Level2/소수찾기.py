import math
from itertools import permutations


def is_prime_number(x):
    if x <= 1:  # 1 제외
        return False

    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False

    return True


def solution(numbers):
    answer = 0
    total_count = len(numbers)

    checked = list()
    for i in range(1, total_count + 1):
        possibles = list(permutations(numbers, i))

        for possible in possibles:
            number_str = ''
            for c in possible:
                number_str += c

            number = int(number_str)
            if number not in checked and is_prime_number(number):
                checked.append(number)
                answer += 1

    return answer


print(solution("011"))
