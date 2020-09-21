import heapq

N, M = map(int, input().split())  # N: 헛간 개수, M: 통로 개수
edges = [[] for _ in range(N + 1)]  # 간선 리스트, 인덱스 0 빼고

# 간선 입력
for _ in range(M):
    s, e = map(int, input().split())
    edges[s].append(e)  # 도착 지점
    edges[e].append(s)  # 양방향

INF = int(1e9)

heap = list()
shortest_list = [INF] * (N + 1)
visited = [False] * (N + 1)

# 1번 시작
shortest_list[1] = 0
heapq.heappush(heap, (0, 1))  # (거리, 노드번호)

# 다익스트라
while heap:
    distance, now = heapq.heappop(heap)
    if visited[now]:  # 이미 방문했으면
        continue

    visited[now] = True
    for destination in edges[now]:
        origin_cost = shortest_list[destination]
        new_cost = distance + 1
        if origin_cost > new_cost:
            heapq.heappush(heap, (new_cost, destination))
            shortest_list[destination] = new_cost

max_distance = max(shortest_list[1:])
to_hide_node = shortest_list.index(max_distance)
to_hide_count = shortest_list.count(max_distance)

print(to_hide_node, max_distance, to_hide_count)







