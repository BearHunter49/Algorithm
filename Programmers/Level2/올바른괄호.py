def solution(s):
    answer = True

    stack = list()

    for c in s:
        if c == '(':
            stack.append(c)
        else:
            if not stack:
                answer = False
                break

            stack.pop()

    if stack:  # 비어있지 않음
        answer = False

    return answer


print(solution("(()("))
