def my_function(number, i, k):
    pivot = number[i]
    last = 0
    for j in range(i - 1, -1, -1):
        if number[j] < pivot:
            k -= 1
        else:
            last = j + 1
            break

        if k == 0:
            last = j
            break

    number = number[:last] + number[i:]
    return number, k, last + 1


def solution(number, k):
    answer = ''

    i = 1
    while True:
        if k == 0:  # 끝
            break

        if len(number) == i:  # 끝까지 봄
            number = number[:-k]
            break

        now = number[i]
        pre = number[i - 1]
        if pre < now:
            number, k, i = my_function(number, i, k)

        else:
            i += 1

    answer = number
    return answer


print(solution("9876", 2))

