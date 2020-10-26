def solution(board):
    row = len(board)
    column = len(board[0])
    answer = 0

    if row == 1:
        answer = 1

    for i in range(1, row):
        for j in range(1, column):
            if board[i][j] == 0:
                continue

            board[i][j] = min(min(board[i - 1][j], board[i][j - 1]), board[i - 1][j - 1]) + 1
            if board[i][j] > answer:
                answer = board[i][j]

    return answer ** 2


print(solution([[0,0,1,1],[1,1,1,1]]))
