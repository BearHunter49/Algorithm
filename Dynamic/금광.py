T = int(input())  # 테스트 케이스 개수

total_result = list()
for _ in range(T):
    N, M = map(int, input().split())
    temp_board = list(map(int, input().split()))

    board = list()
    for i in range(N):
        board.append(temp_board[i * M:(i + 1) * M])

    for j in range(1, M):  # 첫 째 열은 빼고
        for i in range(N):
            first, second, third = 0, 0, 0

            if 0 <= i - 1 < N and 0 <= j - 1 < M:  # 왼쪽 위
                first = board[i - 1][j - 1]
            if 0 <= j - 1 < M:  # 왼쪽
                second = board[i][j - 1]
            if 0 <= i + 1 < N and 0 <= j - 1 < M:  # 왼쪽 아래
                third = board[i + 1][j - 1]

            board[i][j] += max(first, second, third)

    max_result = 0
    for i in range(N):
        max_result = max(max_result, board[i][-1])

    total_result.append(max_result)

for result in total_result:
    print(result)





