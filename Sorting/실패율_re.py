def solution(N, stages):
    answer = []

    users_len = len(stages)
    for i in range(1, N + 1):  # 각 스테이지 마다
        count = stages.count(i)  # 해당 스테이지에 머무르는 사람 수

        fail_rate = 0
        if count == 0:
            fail_rate = 0
        else:
            fail_rate = count / users_len

        users_len -= count  # 다음 남은 유저 수
        answer.append((i, fail_rate))  # (스테이지 번호, 실패율)

    answer.sort(key=lambda x: (-x[1], x[0]))
    answer = [number for number, rate in answer]

    return answer


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))


