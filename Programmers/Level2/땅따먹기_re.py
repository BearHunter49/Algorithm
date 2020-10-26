def solution(land):
    row = len(land)

    for i in range(1, row):
        for j in range(4):
            land[i][j] += max(land[i - 1][:j] + land[i - 1][j + 1:])

    # 마지막 줄 확인
    answer = max(land[-1])

    return answer


print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))
