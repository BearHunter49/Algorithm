N, M = map(int, input().split())
INF = int(1e9)

# 인덱스 0 빼고 시작
graph = [[INF] * (N + 1) for _ in range(N + 1)]

# 대각선은 0으로
for i in range(1, N + 1):
    graph[i][i] = 0

# edge 입력
for _ in range(M):
    s, e = map(int, input().split())
    graph[s][e] = 1  # 어차피 거리는 다 1
    graph[e][s] = 1  # 상호간 연결 돼 있음

X, K = map(int, input().split())  # K 먼저 방문, 그 다음 X 방문

# 플로이드-워셜
for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 항상 1번 회사에서 시작
result = graph[1][K] + graph[K][X]

if result >= INF:
    print(-1)
else:
    print(result)

