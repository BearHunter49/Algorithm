answer = 0


def my_dfs(numbers, index, accumulated, target):
    global answer
    if index == len(numbers):
        if accumulated == target:
            answer += 1
        return

    my_dfs(numbers, index + 1, accumulated + numbers[index], target)
    my_dfs(numbers, index + 1, accumulated - numbers[index], target)


def solution(numbers, target):
    global answer
    my_dfs(numbers, 0, 0, target)

    return answer


print(solution([1, 1, 1, 1, 1], 3))  # 5
