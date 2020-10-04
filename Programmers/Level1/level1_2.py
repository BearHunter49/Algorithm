def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        bin_decoded = bin(arr1[i] | arr2[i])
        decoded = bin_decoded[2:]
        length = len(decoded)

        if length != n:
            decoded = '0' * (n - length) + decoded

        secret_answer = ''
        for c in decoded:
            if c == '0':
                secret_answer += ' '
            else:
                secret_answer += '#'

        answer.append(secret_answer)

    return answer
