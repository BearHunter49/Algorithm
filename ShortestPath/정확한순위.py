N, M = map(int, input().split())  # N: 학생 수, M: 비교 회수
INF = int(1e9)
world = [[INF] * (N + 1) for _ in range(N + 1)]  # 인덱스 0 빼고

# 자기 자신은 0
for i in range(1, N + 1):
    world[i][i] = 0

# 입력
for _ in range(M):
    A, B = map(int, input().split())
    world[A][B] = 1

# 작은놈, 큰놈 리스트
smaller = [0] * (N + 1)
bigger = [0] * (N + 1)

# 플로이드 워셜
for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            world[i][j] = min(world[i][j], world[i][k] + world[k][j])

# 자신보다 큰놈, 작은놈 개수 구하기
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if world[i][j] != INF:
            bigger[i] += 1
            smaller[j] += 1

result = 0
for i in range(1, N + 1):
    if smaller[i] + bigger[i] == N - 1:  # 개수를 다 포함하면
        result += 1

print(result)

# 나는 자기 자신보다 (작은 놈 + 큰 놈) = N - 1(자기 제외) 로 풀었고
# 해설은 현재 자기 자신이 모든 번호와 우위 비교 가능한지(연결이 돼 있는지) 확인
# 원리는 같음






