from collections import deque

N, K = map(int, input().split())  # N: 시험관 크기, K: 바이러스 가지수
board = list()

# 0: 빈칸, 1~: 바이러스 번호
for _ in range(N):
    board.append(list(map(int, input().split())))
S, X, Y = map(int, input().split())  # S: 몇 초 후, X, Y: 좌표

# 바이러스 위치와 종류 찾기
virus_location = list()
virus_kind = set()
for i in range(N):
    for j in range(N):
        if board[i][j] != 0:
            virus_location.append((board[i][j], i, j))  # (바이러스 번호, x, y)
            virus_kind.add(board[i][j])
virus_location.sort(key=lambda x: x[0])  # 바이러스 번호로 오름차순
virus_count = len(virus_kind)  # 바이러스 개수
start_virus_num = virus_location[0][0]

# 초기값
queue = deque()
for location in virus_location:
    queue.append(location)
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # U, R, D, L

for _ in range(S):  # 각 초 마다
    now_count = 1
    now_num = start_virus_num

    while queue:
        virus_num, x, y = queue[0]

        # 싸이클 체크
        if now_num != virus_num:
            now_count += 1
            now_num = virus_num

        if now_count > virus_count:
            break

        # BFS
        queue.popleft()

        for direction in directions:  # 4방향
            n_x = x + direction[0]
            n_y = y + direction[1]

            if 0 <= n_x < N and 0 <= n_y < N and board[n_x][n_y] == 0:  # 범위 안, 빈칸
                board[n_x][n_y] = virus_num  # 전염
                queue.append((virus_num, n_x, n_y))

# 출력
print(board[X - 1][Y - 1])







