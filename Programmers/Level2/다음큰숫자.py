def solution(n):
    n_binary = format(n, 'b')
    one_count = n_binary.count('1')

    answer = n + 1
    while True:
        answer_binary = format(answer, 'b')
        if answer_binary.count('1') == one_count:
            break
        answer += 1

    return answer


print(solution(78))  # 83

