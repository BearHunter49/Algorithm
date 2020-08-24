from collections import deque

N, M = map(int, input().split())
frame = list()
for _ in range(N):
    frame.append(list(map(int, input())))

visited = list()
queue = deque([])
move_list = [(-1, 0), (1, 0), (0, -1), (0, 1)]
count = 0

for x in range(N):
    for y in range(M):
        current_location = (x, y)

        if frame[x][y] == 0 and current_location not in visited:  # 시작점
            queue.append(current_location)
            visited.append(current_location)

            while queue:
                xy = queue.popleft()

                for move in move_list:
                    nx = xy[0] + move[0]
                    ny = xy[1] + move[1]
                    if 0 <= nx < N and 0 <= ny < M and (nx, ny) not in visited and frame[nx][ny] == 0:
                        queue.append((nx, ny))
                        visited.append((nx, ny))

            count += 1

print(count)

