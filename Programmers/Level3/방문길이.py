def solution(dirs):
    answer = 0

    n = 11
    passed = list()
    directions = {
        "U": [-1, 0],
        "L": [0, -1],
        "R": [0, 1],
        "D": [1, 0],
    }
    now = [5, 5]

    for direct in dirs:
        d = directions[direct]
        nx = now[0] + d[0]
        ny = now[1] + d[1]

        if nx < 0 or nx >= n or ny < 0 or ny >= n:  # 맵 경계 밖
            continue

        path = [now[0], now[1], nx, ny]
        path_reverse = [nx, ny, now[0], now[1]]
        if path not in passed and path_reverse not in passed:
            answer += 1
            passed.append(path)
            passed.append(path_reverse)

        now = [nx, ny]

    return answer


print(solution("ULURRDLLU"))  # 7
