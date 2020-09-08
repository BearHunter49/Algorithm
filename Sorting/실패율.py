def solution(N, stages):
    answer = []

    stage_fail_rates = list()  # (stage 번호, 실패율)
    stages.sort()  # 오름차순 정렬
    stage_counting = [0] * (N + 2)  # 인덱스 0과 클리어 스테이지 빼기
    users_len = len(stages)

    # 각 스테이지 머무르는 사람 수
    for stage in stages:
        stage_counting[stage] += 1

    start = 0
    for i in range(users_len):
        stage = stages[i]

        # 실패율 계산
        if stage != start:
            start = stage
            fail_rate = stage_counting[stage] / (users_len - i)
            stage_fail_rates.append((stage, fail_rate))  # 저장

    # 실패율 0인 스테이지
    for i in range(1, N + 1):
        if stage_counting[i] == 0:
            stage_fail_rates.append((i, 0))

    stage_fail_rates.sort(key=lambda x: (-x[1], x[0]))

    for stage_num, rate in stage_fail_rates:
        if stage_num != N + 1:  # 클리어 스테이지는 빼기
            answer.append(stage_num)

    return answer


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))


