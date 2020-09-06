def check_right(u):
    stack = list()
    flag = 0
    for c in u:
        if c == '(':
            stack.append(c)
        else:
            if stack:
                stack.pop()
            else:
                flag = 1
                break

    if flag == 1:
        return False
    else:
        return True


def reverse(string):
    new_string = ''
    for c in string:
        if c == '(':
            new_string += ')'
        else:
            new_string += '('

    return new_string


def solution(p):
    answer = ''

    # 1번
    if p == '':
        return ''

    # 2번
    u = ''
    v = ''
    check = 0
    for i, c in enumerate(p):
        if c == '(':
            check += 1
        else:
            check -= 1
        u = p[:i + 1]
        v = p[i + 1:]

        if check == 0:
            break

    if check_right(u) == True:  # 3 - 1 번
        answer = u + solution(v)
    else:  # 4번
        answer += '('  # 4 - 1
        answer += solution(v)  # 4 - 2
        answer += ')'  # 4 - 3
        answer += reverse(u[1:-1])

    return answer


print(solution("()))((()"))



