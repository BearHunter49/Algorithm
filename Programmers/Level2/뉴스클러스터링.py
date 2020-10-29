def solution(str1, str2):
    str1_words = list()
    str2_words = list()
    for i in range(1, len(str1)):
        one = str1[i - 1].lower()
        two = str1[i].lower()
        if one.isalpha() and two.isalpha():
            str1_words.append(one + two)
    for i in range(1, len(str2)):
        one = str2[i - 1].lower()
        two = str2[i].lower()
        if one.isalpha() and two.isalpha():
            str2_words.append(one + two)

    str1_set = set(str1_words)
    str2_set = set(str2_words)

    intersection = str1_set & str2_set
    union = str1_set | str2_set

    intersection_count = 0
    union_count = 0
    for word in intersection:
        intersection_count += min(str1_words.count(word), str2_words.count(word))
    for word in union:
        union_count += max(str1_words.count(word), str2_words.count(word))

    similarity = 1
    if union_count != 0:
        similarity = intersection_count / union_count

    answer = int(similarity * 65536)

    return answer


print(solution("FRANCE", "french"))  # 16384
