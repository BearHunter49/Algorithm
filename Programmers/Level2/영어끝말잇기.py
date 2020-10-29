def solution(n, words):
    answer = list()

    counts = [0] * n  # 인덱스 0부터 시작. 출력에는 1 더해주어야 함.
    said_list = list()
    turn = 0
    pivot = words[0][0]
    is_failed = 0

    for word in words:
        turn %= n

        if word in said_list or word[0] != pivot:
            answer = [turn + 1, counts[turn] + 1]
            is_failed = 1
            break
        else:
            said_list.append(word)
            counts[turn] += 1
            pivot = word[-1]

        turn += 1

    if is_failed == 0:
        return [0,0]

    return answer


print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))  # [1,3]
