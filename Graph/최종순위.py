# 테스트 케이스 횟수
for _ in range(int(input())):
    n = int(input())  # 팀의 개수
    past_order = list(map(int, input().split()))  # i: 등수

    m = int(input())  # 등수가 바뀐 쌍 개수

    changed = list()
    for _ in range(m):
        a, b = map(int, input().split())
        changed.append((a, b))

    teams = [(-1, -1, -1) for _ in range(n + 1)]  # 팀의 아래 팀 개수 정보, 인덱스 0 뺌

    for i in range(n):
        team_number = past_order[i]
        teams[team_number] = (team_number, i + 1, (n - 1) - i)  # (팀 번호, 원래 등수, indegree)

    # 변동 순위 적용
    for a, b in changed:
        a_num, a_past_rank, a_indegree = teams[a]
        b_num, b_past_rank, b_indegree = teams[b]

        if a_past_rank < b_past_rank:  # a가 더 높았음
            teams[a] = (a, a_past_rank, a_indegree - 1)
            teams[b] = (b, b_past_rank, b_indegree + 1)
        else:  # b가 더 높았음
            teams[a] = (a, a_past_rank, a_indegree + 1)
            teams[b] = (b, b_past_rank, b_indegree - 1)

    teams.sort(key=lambda x: -x[2])  # indegree 내림차순 정렬

    # 불가능한 경우
    is_possible = True
    pre_degree = teams[0][2]
    for i in range(1, n):
        in_degree = teams[i][2]
        if pre_degree == in_degree:  # indegree 같은게 있으면 불가능함
            is_possible = False
            break

    # 출력
    if is_possible:
        for i in range(0, n):
            print(teams[i][0], end=' ')
    else:
        print("IMPOSSIBLE")







