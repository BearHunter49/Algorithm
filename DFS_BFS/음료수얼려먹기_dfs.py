N, M = map(int, input().split())
frame = list()
for _ in range(N):
    frame.append(list(map(int, input())))

move_list = [(-1, 0), (1, 0), (0, -1), (0, 1)]
count = 0


def dfs(x, y):
    # break 조건
    if x < 0 or x >= N or y < 0 or y >= M:
        return False

    # DFS
    if frame[x][y] == 0:
        frame[x][y] = 1
        for move in move_list:
            dfs(x + move[0], y + move[1])
        return True

    return False


for x in range(N):
    for y in range(M):
        if dfs(x, y):
            count += 1

print(count)

# DFS 나 BFS 나 O(N) - 탐색이니까
