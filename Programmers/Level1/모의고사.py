def solution(answers):
    answer = []

    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    solved = [0, 0, 0]

    for i, number in enumerate(answers):
        if number == one[i % 5]:
            solved[0] += 1
        if number == two[i % 8]:
            solved[1] += 1
        if number == three[i % 10]:
            solved[2] += 1

    max_num = max(solved)
    for index, count in enumerate(solved):
        if count == max_num:
            answer.append(index + 1)

    return answer


print(solution([1, 2, 3, 4, 5]))