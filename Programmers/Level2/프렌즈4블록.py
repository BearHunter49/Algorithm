def check_four(board, x, y):
    pivot = board[x][y]
    for i in range(x, x + 2):
        for j in range(y, y + 2):
            if board[i][j] != pivot:
                return False
    return True


def do_erase(board, x, y):
    for i in range(x, x + 2):
        for j in range(y, y + 2):
            board[i][j] = '0'


def find_next_block(board, x, y):
    for i in range(x - 1, -1, -1):
        if board[i][y] != '0':
            return i, y

    return -1, -1


def push_block(board):
    m = len(board)
    n = len(board[0])

    for j in range(n):
        for i in range(m - 1, -1, -1):
            if board[i][j] == '0':
                x, y = find_next_block(board, i, j)
                if x == -1 and y == -1:
                    break
                board[i][j] = board[x][y]
                board[x][y] = '0'


def find_erased_block(board):
    m = len(board)
    n = len(board[0])
    result = 0
    for i in range(m):
        for j in range(n):
            if board[i][j] == '0':
                result += 1
    return result


def solution(m, n, board):
    new_board = list()
    for string in board:
        new_board.append(list(string))

    while True:
        erased_point = list()  # [[x, y], ...]

        # search
        has_erase = 0
        for i in range(m - 1):
            for j in range(n - 1):
                if new_board[i][j] != '0' and check_four(new_board, i, j):
                    has_erase = 1
                    erased_point.append([i, j])

        if has_erase == 0:
            break

        # erase
        for x, y in erased_point:
            do_erase(new_board, x, y)

        # push
        push_block(new_board)

    answer = find_erased_block(new_board)

    return answer


print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))  # 14
