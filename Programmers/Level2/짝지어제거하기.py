def solution(s):
    answer = 0

    stack = list()
    for c in s:
        if not stack:
            stack.append(c)
        else:
            if stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)

    if not stack:
        answer = 1

    return answer


print(solution("b"))
