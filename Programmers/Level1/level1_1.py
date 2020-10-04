def solution(n):
    answer = ''

    q, r = divmod(n, 2)
    answer += '수박' * q + '수' * r


    return answer
