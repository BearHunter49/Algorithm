import math
from functools import reduce


# 최소공배수 함수
def my_lcm(a, b):  # Least Common Multiplier
    return int((a * b) / (math.gcd(a, b)))


def solution(arr):
    answer = reduce(my_lcm, arr)
    return answer


print(solution([2,6,8,14]))  # 168
