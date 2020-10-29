import math


def solution(n, a, b):
    my_round = 0

    while True:
        my_round += 1

        a = math.ceil(a / 2)
        b = math.ceil(b / 2)

        if a == b:
            break

    return my_round


print(solution(8,4,7))  # 3
