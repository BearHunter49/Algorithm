from collections import deque

# 테스트 케이스 횟수
for _ in range(int(input())):
    n = int(input())  # 팀의 개수

    # 인덱스 0 뺌
    in_degree_list = [0] * (n + 1)  # 진입차수 리스트
    edges = [[] for _ in range(n + 1)]  # 간선정보

    past_rank = list(map(int, input().split()))  # i: 등수
    m = int(input())  # 등수가 바뀐 쌍 개수

    # 진입차수와 간선정보
    for i in range(n - 1):
        win_team = past_rank[i]
        for j in range(i + 1, n):
            lose_team = past_rank[j]

            edges[lose_team].append(win_team)  # 진 팀이 이긴 팀을 바라봄
            in_degree_list[win_team] += 1  # 이긴 팀 진입차수 증가

    # 순위 변동 입력
    for _ in range(m):
        a, b = map(int, input().split())

        if b in edges[a]:  # a -> b 였으면
            # b -> a 로 바꾸기
            edges[b].append(a)
            edges[a].remove(b)

            in_degree_list[b] -= 1
            in_degree_list[a] += 1
        else:  # b -> a 였으면
            # a -> b 로 바꾸기
            edges[a].append(b)
            edges[b].remove(a)

            in_degree_list[a] -= 1
            in_degree_list[b] += 1

    # Topology
    start = 0
    for i in range(1, n + 1):
        if in_degree_list[i] == 0:
            start = i
            break

    queue = deque()
    queue.append(start)

    total_count = n
    fail_flag = 0
    result = list()  # 순위 낮은 순서
    while queue:
        team = queue.popleft()
        total_count -= 1
        result.append(team)

        zero_count = 0
        for dest_team in edges[team]:
            in_degree_list[dest_team] -= 1
            if in_degree_list[dest_team] == 0:  # 0되면 큐에 넣기
                queue.append(dest_team)
                zero_count += 1

            if zero_count > 1:  # 진입차수 0이 2개 이상
                fail_flag = 1
                break

    if fail_flag == 1:  # 순위 알 수 없음
        print("?")
        continue

    if total_count != 0:  # 정보 이상함
        print("IMPOSSIBLE")
        continue

    # 출력
    result = result[::-1]  # 순위 높은 순서로
    for team in result:
        print(team, end=' ')



