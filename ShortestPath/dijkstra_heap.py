import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())
start = int(input())
graph = [[] for _ in range(N + 1)]  # 간선 그래프
visited = [False] * (N + 1)  # 방문 리스트
shortest_distance = [INF] * (N + 1)  # 최단거리 리스트
heap = []  # 힙 리스트

# 간선 입력받기
for _ in range(M):
    s, e, d = map(int, input().split())
    graph[s].append((e, d))

# 시작점
shortest_distance[start] = 0
heapq.heappush(heap, (0, start))

# 알고리즘
while heap:
    # 현재 노드 선택하기
    now_distance, now_index = heapq.heappop(heap)
    if visited[now_index] == True:  # 방문 안한 경우만 알고리즘 실행
        continue

    # 다익스트라
    visited[now_index] = True
    for edge in graph[now_index]:
        destination = edge[0]
        distance = edge[1]

        origin_cost = shortest_distance[destination]
        new_cost = now_distance + distance

        if origin_cost > new_cost:  # 새로운게 더 짧으면
            shortest_distance[destination] = new_cost
            heapq.heappush(heap, (new_cost, destination))

for i in range(1, N + 1):
    if shortest_distance[i] == INF:
        print("도달 불가")
    else:
        print(shortest_distance[i])

# O(ElogV)
# 모든 간선을 힙에 넣었다 빼는 경우 O(ElogE)
# 하지만 간선의 개수는 최대 V^2개 가능
# 따라서 O(ElogV)








