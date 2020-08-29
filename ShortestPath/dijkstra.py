import sys
input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())
start = int(input())
graph = [[] for _ in range(N + 1)]  # 간선 그래프
visited = [False] * (N + 1)  # 방문 리스트
shortest_distance = [INF] * (N + 1)  # 최단거리 리스트

# 간선 입력받기
for _ in range(M):
    s, e, d = map(int, input().split())
    graph[s].append((e, d))


# 알고리즘
shortest_distance[start] = 0
for _ in range(N):
    # 현재 노드 선택하기
    now_index = 0
    for i in range(1, N + 1):
        if visited[i] == False and shortest_distance[now_index] > shortest_distance[i]:  # 방문 안했고, 가장 짧으면
            now_index = i

    # 다익스트라
    visited[now_index] = True
    for edge in graph[now_index]:
        destination = edge[0]
        distance = edge[1]

        origin_cost = shortest_distance[destination]
        new_cost = shortest_distance[now_index] + distance

        shortest_distance[destination] = min(origin_cost, new_cost)

for i in range(1, N + 1):
    if shortest_distance[i] == INF:
        print("도달 불가")
    else:
        print(shortest_distance[i])

# O(V^2) - min 선형탐색 O(V), 각 노드에 연결 돼 있는 간선 확인 O(V)

