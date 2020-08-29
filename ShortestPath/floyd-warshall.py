N = int(input())
M = int(input())

INF = int(1e9)
graph = [[INF] * (N + 1) for _ in range(N + 1)]  # 인덱스 1 부터

for i in range(1, N + 1):  # 자기자신 0으로
    graph[i][i] = 0

for _ in range(M):  # 입력
    s, e, d = map(int, input().split())
    graph[s][e] = d

# 플로이드-워셜
for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    # 단계별 출력
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            print(graph[i][j], end=' ')
        print()
    print()

# O(V^3)


