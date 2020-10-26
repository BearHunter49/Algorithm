def solution(x):
    answer = True

    total = 0
    for c in str(x):
        total += int(c)

    if x % total != 0:
        answer = False

    return answer


print(solution(11))
