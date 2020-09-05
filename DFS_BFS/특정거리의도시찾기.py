from collections import deque

# N: 도시 개수, M: 도로 개수, K: 찾을 거리, X: 출발 도시 번호
N, M, K, X = map(int, input().split())

# 인덱스 0 없음
edges = [[] for _ in range(N + 1)]

for _ in range(M):
    s, e = map(int, input().split())
    edges[s].append(e)  # 연결 지점

# BFS 쓰기
queue = deque([])

# 초기값
queue.append((X, 0))  # (도시 번호, 여태 거리)
INF = int(1e9)
city_distance = [INF] * (N + 1)  # 각 도시 최단거리 저장
city_distance[X] = 0  # 출발점은 0

while queue:
    now_city, now_distance = queue.popleft()

    # 연결된 도시들 큐에 넣기
    for destination in edges[now_city]:
        n_distance = now_distance + 1  # 다음 도시까지 거리

        if city_distance[destination] > n_distance:  # 거리가 더 작을때만
            city_distance[destination] = n_distance
            queue.append((destination, n_distance))

# 출력
flag = 0
for i in range(N + 1):
    if city_distance[i] == K:
        flag = 1
        print(i)

if flag == 0:  # K 거리인 도시가 하나도 없으면
    print(-1)












