from collections import deque

N = int(input())  # 보드 크기 (정사각형)
K = int(input())  # 사과 개수

board = [[0] * (N + 1) for _ in range(N + 1)]  # 보드 판, 인덱스 0 빼고 함
# 0은 길, 1은 뱀, 2는 사과
for _ in range(K):
    x, y = map(int, input().split())
    board[x][y] = 2

L = int(input())  # 뱀 방향전환 횟수
turn_list = list()
for _ in range(L):
    s, d = input().split()
    turn_list.append((int(s), d))  # (시간 초, 바꿀 방향)

board[1][1] = 1  # (1, 1)에서 뱀 출발
snake_queue = deque([(1, 1)])  # 뱀 큐

# 현재 방향에서 D(오른쪽)은 +1, L(왼쪽)은 -1
direction_order = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # U, R, D, L 순
now_direction = 1  # 현재 진행 방향
now_time = 0

# 시작
while True:
    now_time += 1  # 1초 씩 보기
    now = snake_queue[-1]  # 현재 좌표
    n_x, n_y = now[0] + direction_order[now_direction][0], now[1] + direction_order[now_direction][1]  # 한 칸 진행

    # 맵 벗어나는 경우 끝
    if n_x < 1 or n_x > N or n_y < 1 or n_y > N:
        break

    # 시간 지난 뒤 방향 전환
    for turn in turn_list:
        if turn[0] == now_time:  # 방향 바꿔야 하면

            if turn[1] == "L":  # 왼쪽
                now_direction = (now_direction - 1) % 4
            else:  # 오른쪽
                now_direction = (now_direction + 1) % 4

    if board[n_x][n_y] == 2:  # 사과라면 머리만 늘리기
        snake_queue.append((n_x, n_y))
        board[n_x][n_y] = 1  # 뱀 머리로 덮기

    elif board[n_x][n_y] == 0:  # 길이면 머리 늘리고 꼬리 줄이기
        snake_queue.append((n_x, n_y))
        shrink_x, shrink_y = snake_queue.popleft()
        board[n_x][n_y] = 1  # 뱀 머리로 덮기
        board[shrink_x][shrink_y] = 0  # 꼬리 없애기

    else:  # 뱀 몸체면 끝내기
        break

print(now_time)







