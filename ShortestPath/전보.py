import heapq

# V 개수가 3만개 이므로, 다익스트라로 풀기
N, M, C = map(int, input().split())
INF = int(1e9)

# 인덱스 0 빼고 시작
graph = [[] for _ in range(N + 1)]
shortest_distance = [INF] * (N + 1)
visited = [False] * (N + 1)

# 간선 입력
for _ in range(M):
    s, e, d = map(int, input().split())
    graph[s].append((e, d))

# 초기값
heap = list()
shortest_distance[C] = 0
heapq.heappush(heap, (0, C))  # (최단거리, 노드)

while heap:
    now_distance, now_index = heapq.heappop(heap)

    # 이미 방문 했으면 넘기기
    if visited[now_index] == True:
        continue

    # 다익스트라
    visited[now_index] = True
    for edge in graph[now_index]:
        destination = edge[0]
        distance = edge[1]

        origin_cost = shortest_distance[destination]
        new_cost = now_distance + distance

        if new_cost < origin_cost:  # 갱신
            shortest_distance[destination] = new_cost
            heapq.heappush(heap, (new_cost, destination))

total_count = 0
total_time = 0
for d in shortest_distance:
    if 0 < d < INF:
        total_count += 1
        total_time = max(d, total_time)

print(total_count, total_time)







