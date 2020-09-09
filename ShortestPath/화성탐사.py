import heapq

T = int(input())
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # U, R, D, L
INF = int(1e9)

for _ in range(T):  # 테스트 케이스
    N = int(input())  # 화성 크기
    edges = [[] for _ in range(N * N)]  # N^2 개의 노드 (인덱스 0 포함)
    world = list()  # 화성지도

    # 맵 입력
    for _ in range(N):
        world.append(list(map(int, input().split())))

    # 간선 정보 입력
    for i in range(N):
        for j in range(N):

            now = (N * i) + j
            for x, y in directions:  # 모든 방향에 대해
                n_x = i + x
                n_y = j + y

                if 0 <= n_x < N and 0 <= n_y < N:  # world 안쪽이면
                    next_node = (N * n_x) + n_y
                    edges[now].append((next_node, world[n_x][n_y]))  # (다음 노드 번호, 가는 비용)

    # 다익스트라 (0번 노드 -> N*N - 1번 노드)
    shortest_list = [INF] * (N * N)
    visited = [False] * (N * N)  # 방문 리스트

    shortest_list[0] = world[0][0]  # 시작 노드
    heap = list()

    heapq.heappush(heap, (shortest_list[0], 0))  # (최단거리, 노드번호)

    while heap:
        now_cost, now_node = heapq.heappop(heap)

        if visited[now_node] == True:  # 이미 방문 했으면
            continue
        else:
            visited[now_node] = True  # 방문처리

            for next_node, next_cost in edges[now_node]:
                new_cost = now_cost + next_cost
                original_cost = shortest_list[next_node]

                if new_cost < original_cost:  # 거리가 더 짧으면
                    shortest_list[next_node] = new_cost  # 갱신
                    heapq.heappush(heap, (new_cost, next_node))

    print(shortest_list[-1])

# 해설지는 shortest_list를 2차원 배열로 (0, 0)에서 (x, y)까지 가는 최단거리를 저장함



