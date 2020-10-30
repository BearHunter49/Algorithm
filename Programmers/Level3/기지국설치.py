import math


def get_remained(n, stations, w):
    remained = list()
    tail = 1
    for station in stations:
        pre = station - w
        post = station + w + 1

        if pre < 0:
            pre = 1
        if pre > tail:
            remained.append([tail, pre])
        tail = post

    if tail < n + 1:
        remained.append([tail, n + 1])
    return remained


def solution(n, stations, w):
    answer = 0

    remained = get_remained(n, stations, w)
    for start, end in remained:
        distance = end - start
        answer += math.ceil(distance / (w * 2 + 1))

    return answer


print(solution(11, [4, 11], 1))  # 3
