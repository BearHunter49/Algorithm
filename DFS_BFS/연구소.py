from collections import deque
from itertools import combinations
import copy

N, M = map(int, input().split())

board = list()
for _ in range(N):
    board.append(list(map(int, input().split())))

# 0: 빈칸, 1: 벽, 2: 바이러스
queue = deque()
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # U, R, D, L

virus_location = list()
void_location = list()

# 바이러스와 빈칸 위치 저장
for i in range(N):
    for j in range(M):
        if board[i][j] == 2:
            virus_location.append((i, j))
        if board[i][j] == 0:
            void_location.append((i, j))

possibles = list(combinations(void_location, 3))  # 벽 세우는 모든 경우의 수
answer = 0  # 답

for possible in possibles:  # 모든 벽 가능성에 대해
    temp_board = copy.deepcopy(board)  # 새 보드

    # 벽 세우기
    for p in possible:
        temp_board[p[0]][p[1]] = 1

    # 바이러스 퍼트리기
    for x, y in virus_location:
        queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for direction in directions:  # 모든 방향에 대해
            n_x = x + direction[0]
            n_y = y + direction[1]

            if 0 <= n_x < N and 0 <= n_y < M and temp_board[n_x][n_y] == 0:  # 빈칸이면 퍼트리기
                temp_board[n_x][n_y] = 2
                queue.append((n_x, n_y))

    # 빈칸 개수 세기
    count = 0
    for row in temp_board:
        for state in row:
            if state == 0:
                count += 1

    # 최소 찾기
    answer = max(answer, count)

print(answer)











