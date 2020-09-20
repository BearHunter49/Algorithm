from collections import deque

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # U, R, D, L


def possible_next(position, board):
    possible_list = list()
    position = list(position)
    x1, y1 = position[0][0], position[0][1]
    x2, y2 = position[1][0], position[1][1]

    # 4방향 확인
    for dx, dy in directions:
        nx1, ny1 = x1 + dx, y1 + dy
        nx2, ny2 = x2 + dx, y2 + dy

        if board[nx1][ny1] != 1 and board[nx2][ny2] != 1:
            possible_list.append({(nx1, ny1), (nx2, ny2)})

    # 회전 확인
    if x1 == x2:  # 드론 가로방향
        for d in [-1, 1]:  # -1: 위, 1: 아래
            if board[x1 + d][y1] != 1 and board[x2 + d][y2] != 1:
                possible_list.append({(x1, y1), (x1 + d, y1)})
                possible_list.append({(x2, y2), (x2 + d, y2)})

    else:  # 드론 세로방향
        for d in [-1, 1]:  # -1: 왼쪽, 1: 오른쪽
            if board[x1][y1 + d] != 1 and board[x2][y2 + d] != 1:
                possible_list.append({(x1, y1), (x1, y1 + d)})
                possible_list.append({(x2, y2), (x2, y2 + d)})

    return possible_list


def solution(board):
    answer = 0
    n = len(board)
    new_board = [[1] * (n + 2) for _ in range(n + 2)]  # 외벽 확장
    queue = deque()

    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]

    start = {(1, 1), (1, 2)}  # 시작 좌표
    visited = list()  # 드론 방문 좌표 리스트

    queue.append((start, 0))  # (드론 좌표, 이동시간)

    while queue:
        position, time = queue.popleft()

        # 도착 확인
        if (n, n) in position:
            answer = time
            break

        for possible in possible_next(position, new_board):
            if possible not in visited:  # 방문 한 적 없음
                queue.append((possible, time + 1))
                visited.append(possible)

    return answer


print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))

# 집합 자료형만 in 으로 중복 확인 가능
# {(1, 1), (1, 2)} 와 {(1, 2), (1, 1)} 같은거 처리









