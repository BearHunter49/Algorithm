N, M = map(int, input().split())
x, y, d = map(int, input().split())

world = list()
for _ in range(N):
    world.append(list(map(int, input().split())))

# 0: 북, 1: 동, 2: 남, 3: 서
d_move = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# 밟은 발판
visited = [(x, y)]

# start
patience = 0
while True:
    next_move = d_move[d - 1]
    d = d_move.index(next_move)

    nx = x + next_move[0]
    ny = y + next_move[1]

    if world[nx][ny] == 0 and (nx, ny) not in visited:  # 가보지 않은 칸
        visited.append((nx, ny))
        x = nx
        y = ny
        patience = 0
        
    else:  # 가본 칸
        patience += 1

    # 4 방면이 못 가는 경우
    if patience == 4:
        next_move = d_move[d - 2]
        nx = x + next_move[0]
        ny = y + next_move[1]

        if world[nx][ny] == 0:  # 육지이면
            x = nx
            y = ny
            patience = 0
        else:  # 바다이면
            break

print(len(visited))






