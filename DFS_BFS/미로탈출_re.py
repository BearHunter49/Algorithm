from collections import deque

N, M = map(int, input().split())

world = list()
for _ in range(N):
    world.append(list(map(int, input())))

# 시작지점 (1, 1) -> (0, 0) 으로 계산
queue = deque([(0, 0, 0)])  # 시작지점 (x, y, count)

move_list = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우
result = 0

while queue:
    location = queue.popleft()
    x = location[0]
    y = location[1]
    count = location[2]

    if world[x][y] == 1:  # 갈 수 있는 길
        world[x][y] = 0
        count += 1
    else:  # 막힌 길
        continue

    if x == N - 1 and y == M - 1:  # 도착
        result = count
        break

    for move in move_list:
        nx = x + move[0]
        ny = y + move[1]
        if 0 <= nx < N and 0 <= ny < M:  # 맵 경계
            queue.append((nx, ny, count))

print(result)
