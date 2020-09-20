directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # U, R, D, L


# 시계방향 회전
def turn_clockwise(pivot: tuple, other: tuple, hor_or_ver: int):
    blocked = tuple()
    if hor_or_ver == -1:  # 가로방향
        if pivot[1] < other[1]:  # 왼쪽 축
            other = (other[0] + 1, other[1] - 1)
            blocked = (other[0] + 1, other[1])
        else:  # 오른쪽 축
            other = (other[0] - 1, other[1] + 1)
            blocked = (other[0] - 1, other[1])
    else:  # 세로방향
        if pivot[0] < other[0]:  # 위쪽 축
            other = (other[0] - 1, other[1] - 1)
            blocked = (other[0], other[1] - 1)
        else:  # 아래쪽 축
            other = (other[0] + 1, other[1] + 1)
            blocked = (other[0], other[1] + 1)

    return [pivot, other], blocked


# 반시계방향 회전
def turn_counter_clockwise(pivot: tuple, other:tuple, hor_or_ver: int):
    blocked = tuple()
    if hor_or_ver == -1:  # 가로방향
        if pivot[1] < other[1]:  # 왼쪽 축
            other = (other[0] - 1, other[1] - 1)
            blocked = (other[0] - 1, other[1])
        else:  # 오른쪽 축
            other = (other[0] + 1, other[1] + 1)
            blocked = (other[0] + 1, other[1])
    else:  # 세로방향
        if pivot[0] < other[0]:  # 위쪽 축
            other = (other[0] - 1, other[1] + 1)
            blocked = (other[0], other[1] + 1)
        else:  # 아래쪽 축
            other = (other[0] + 1, other[1] - 1)
            blocked = (other[0], other[1] - 1)

    return [pivot, other], blocked


# 지나온 곳 표시할 좌표
def passed(origin_location, new_location):
    past = set(origin_location) - set(new_location)
    return list(past)


def is_possible(loc1, loc2, board):
    x1, y1 = loc1
    x2, y2 = loc2
    size = len(board)

    if 0 <= x1 < size and 0 <= y1 < size and 0 <= x2 < size and 0 <= y2 < size and\
            board[x1][y1] != 1 and board[x2][y2] != 1:  # 맵 경계, 벽 확인
        return True
    else:
        return False


# 탐색 알고리즘
def dfs(drone_location: list, hor_or_ver: int, board, answer):
    x1, y1 = drone_location[0]
    x2, y2 = drone_location[1]
    n = len(board)

    # 도착 체크
    if (x1 == n - 1 and y1 == n - 1) or (x2 == n - 1 and y2 == n - 1):
        return answer

    # 4방향 확인
    min_count = int(1e9)
    for dx, dy in directions:
        nx1, ny1 = x1 + dx, y1 + dy
        nx2, ny2 = x2 + dx, y2 + dy
        new_location = [(nx1, ny1), (nx2, ny2)]

        if is_possible(new_location[0], new_location[1], board):
            passed_location = passed(drone_location, new_location)

            # 지나쳐온 곳 표시
            for px, py in passed_location:
                board[px][py] = 1

            count = dfs(new_location, hor_or_ver, board, answer + 1)

            # 지나쳐온 곳 복구
            for px, py in passed_location:
                board[px][py] = 0

            if count < min_count:
                min_count = count

    # 회전 확인
    # 각 축의 시계방향 회전
    for _ in range(2):
        turned_location, blocked = turn_clockwise(drone_location[0], drone_location[1], hor_or_ver)

        if is_possible(turned_location[0], turned_location[1], board) and\
                is_possible(turned_location[0], blocked, board):
            passed_location = passed(drone_location, turned_location)
            hor_or_ver *= -1

            # 지나쳐온 곳 표시
            for px, py in passed_location:
                board[px][py] = 1

            count = dfs(turned_location, hor_or_ver, board, answer + 1)

            # 지나쳐온 곳 복구
            for px, py in passed_location:
                board[px][py] = 0

            if count < min_count:
                min_count = count

            # 축 바꾸기
            drone_location[0], drone_location[1] = drone_location[1], drone_location[0]

    # 각 축의 반시계방향 회전
    for _ in range(2):
        turned_location, blocked = turn_counter_clockwise(drone_location[0], drone_location[1], hor_or_ver)

        if is_possible(turned_location[0], turned_location[1], board) and\
                is_possible(turned_location[0], blocked, board):
            passed_location = passed(drone_location, turned_location)
            hor_or_ver *= -1

            # 지나쳐온 곳 표시
            for px, py in passed_location:
                board[px][py] = 1

            count = dfs(turned_location, hor_or_ver, board, answer + 1)

            # 지나쳐온 곳 복구
            for px, py in passed_location:
                board[px][py] = 0

            if count < min_count:
                min_count = count

            # 축 바꾸기
            drone_location[0], drone_location[1] = drone_location[1], drone_location[0]

    return min_count


def solution(board):
    answer = 0
    drone_location = [(0, 0), (0, 1)]  # 드론 몸체 (x1, y1), (x2, y2)
    hor_or_ver = -1  # -1: horizontal, 1: vertical

    # 출발
    answer = dfs(drone_location, hor_or_ver, board, answer)

    return answer


print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))








