N = int(input())  # 도시 개수
M = int(input())  # 버스 개수(간선 개수)

INF = int(1e9)
world = [[INF] * (N + 1) for _ in range(N + 1)]  # 인덱스 0 빼기

# 자기자신은 거리가 0
for i in range(1, N + 1):
    world[i][i] = 0

# 간선 입력
for _ in range(M):
    a, b, c = map(int, input().split())
    world[a][b] = min(world[a][b], c)

# 플로이드 워셜
for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            world[i][j] = min(world[i][j], world[i][k] + world[k][j])

# 출력
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if world[i][j] == INF:
            print(0, end=' ')
        else:
            print(world[i][j], end=' ')
            
    print()

