def solution(number, k):
    answer = ''

    stack = list()
    for num in number:
        while stack and num > stack[-1] and k > 0:
            stack.pop()
            k -= 1
        stack.append(num)

    answer = ''.join(stack)
    if k > 0:
        answer = answer[:-k]
    return answer


print(solution("428584", 2))

