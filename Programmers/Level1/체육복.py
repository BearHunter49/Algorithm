def solution(n, lost, reserve):
    answer = 0
    students = [1] * (n + 2)  # 인덱스 0, n + 1 빼고
    students[0] = -1
    students[n + 1] = -1

    for num in lost:
        students[num] -= 1
    for num in reserve:
        students[num] += 1

    for i in range(1, n + 1):  # 1 ~ n
        have = students[i]
        if have == 1:
            answer += 1
        elif have == 2:
            answer += 1
            if students[i - 1] == 0:  # 왼쪽부터 빌려주기
                students[i - 1] = 1
                answer += 1
            elif students[i + 1] == 0:  # 오른쪽
                students[i + 1] = 1

    return answer


print(solution(5, [2, 4], [1, 3, 5]))  # 5

