N = int(input())  # 복도 크기
board = list()
result = False

# 입력
for _ in range(N):
    board.append(input().split())

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # U, D, L, R
students_location = list()

for i in range(N):
    for j in range(N):
        if board[i][j] == 'S':
            students_location.append((i, j))  # 학생의 (x, y) 좌표 저장


# 장애물 설치 재귀함수
def set_obstacle(count):
    global result

    # 장애물 모두 설치한 경우
    if count == 3:
        for stu_x, stu_y in students_location:
            for d_x, d_y in directions:

                # 해당 방향으로 선생님 있나 확인
                n_x, n_y = stu_x, stu_y
                is_discovered = 0
                while True:
                    n_x += d_x
                    n_y += d_y

                    # 맵 경계
                    if n_x < 0 or n_x >= N or n_y < 0 or n_y >= N:
                        break

                    # 선생한테 발각
                    if board[n_x][n_y] == 'T':
                        is_discovered = 1
                        break

                    # 장애물에 막히면
                    if board[n_x][n_y] == 'O':
                        break

                if is_discovered == 1:  # 선생한테 발각
                    return

        # 한번이라도 발각 안됐으면
        result = True
        return

    # 장애물 설치
    for i in range(N):
        for j in range(N):
            if board[i][j] == 'X':
                board[i][j] = 'O'  # 설치
                count += 1

                set_obstacle(count)

                # 한 번이라도 성공했으면 빨리 멈추기
                if result == True:
                    return

                board[i][j] = 'X'  # 다시 회수
                count -= 1


set_obstacle(0)
if result == True:
    print("YES")
else:
    print("NO")






