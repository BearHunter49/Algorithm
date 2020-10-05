answer = int(1e9)


def is_length_one(now, word):
    diff = 0
    for c1, c2 in zip(now, word):
        if c1 != c2:
            diff += 1

    if diff == 1:
        return True
    return False


def find_by_dfs(now, target, words, checked, count):
    global answer

    if now == target:  # 찾음
        answer = min(answer, count)

    for word in words:
        if is_length_one(now, word) and word not in checked:
            checked.append(word)
            find_by_dfs(word, target, words, checked, count + 1)
            checked.remove(word)


def solution(begin, target, words):
    global answer

    checked = list()
    find_by_dfs(begin, target, words, checked, 0)
    if answer == int(1e9):
        answer = 0

    return answer


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))