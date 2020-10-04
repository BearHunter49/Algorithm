def solution(brown, yellow):
    answer = []

    width_add_height = (brown + 4) // 2
    for i in range(1, 2502):
        for j in range(1, 2502 - i):
            if (i + j) == width_add_height and ((i - 2) * (j - 2)) == yellow:
                answer.append(i)
                answer.append(j)
                answer.sort(reverse=True)
                return answer

    return answer


print(solution(10, 2))