from collections import deque

N = int(input())  # 보드 크기
K = int(input())  # 사과 크기

board = [[0] * N for _ in range(N)]  # 인덱스 0 시작
board[0][0] = 1  # 뱀 시작점

for _ in range(K):  # 사과 입력
    x, y = map(int, input().split())
    board[x - 1][y - 1] = 2  # 2: 사과

L = int(input())  # 방향 전환 횟수
turn_info = deque()  # (시간, 방향전환)
for _ in range(L):
    time, direction = input().split()
    turn_info.append((int(time), direction))

snake = deque()  # 왼쪽: 꼬리, 오른쪽: 머리
time = 0

snake.append((0, 0))  # 출발점
now_direction = 1  # R
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # U, R, D, L

while True:
    time += 1
    head_x, head_y = snake[-1][0], snake[-1][1]
    tail_x, tail_y = snake[0][0], snake[0][1]

    n_x, n_y = head_x + directions[now_direction][0], head_y + directions[now_direction][1]

    if 0 <= n_x < N and 0 <= n_y < N and board[n_x][n_y] != 1:  # 벽, 뱀 확인
        if board[n_x][n_y] == 0:  # 그냥 길이면 꼬리 줄이기
            board[tail_x][tail_y] = 0
            snake.popleft()

        board[n_x][n_y] = 1
        snake.append((n_x, n_y))

    else:  # 게임 끝
        break

    # 초가 끝난 뒤
    if turn_info and time == turn_info[0][0]:  # 방향전환 정보
        info = turn_info.popleft()
        turn = info[1]
        if turn == 'L':
            now_direction = (now_direction - 1) % 4
        else:
            now_direction = (now_direction + 1) % 4

print(time)

