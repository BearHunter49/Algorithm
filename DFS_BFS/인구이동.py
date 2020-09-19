from collections import deque

N, L, R = map(int, input().split())  # N: 나라 크기, L <= 연합조건 <= R

populations = list()  # 인구수 2차원 배열
for _ in range(N):
    populations.append(list(map(int, input().split())))

queue = deque()
count = 0
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # U, R, D, L


# 연합 찾아보기
def process(i, j, check_union):
    union = list()  # 연합들 좌표
    populations_sum = 0  # 연합들 인구수 합
    check = 0

    # 연합 가입
    check_union[i][j] = 1
    populations_sum += populations[i][j]
    union.append((i, j))

    queue.append((i, j))  # (x, y)

    while queue:
        x, y = queue.popleft()

        for d_x, d_y in directions:
            nx = x + d_x
            ny = y + d_y

            if 0 <= nx < N and 0 <= ny < N and check_union[nx][ny] != 1:  # 아직 연합 체크 안한 경우
                if L <= abs(populations[x][y] - populations[nx][ny]) <= R:  # 연합 가능

                    # 연합 가입
                    check_union[nx][ny] = 1
                    populations_sum += populations[nx][ny]
                    union.append((nx, ny))

                    queue.append((nx, ny))
                    check = 1

    # 인구 이동
    new_population = populations_sum // len(union)
    for x, y in union:
        populations[x][y] = new_population

    return check


while True:
    check_union = [[0] * N for _ in range(N)]  # 연합 지도
    flag = 0

    # 1 싸이클
    for i in range(N):
        for j in range(N):
            if check_union[i][j] != 1:
                if process(i, j, check_union) == 1:  # 한 번이라도 연합 됐는지 체크
                    flag = 1

    if flag == 1:
        count += 1
    else:  # 연합이 없었으면
        break

# 출력
print(count)













