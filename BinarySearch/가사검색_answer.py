from bisect import bisect_left, bisect_right


def count_by_range(arr, left, right):
    left_index = bisect_left(arr, left)
    right_index = bisect_right(arr, right)

    return right_index - left_index


def solution(words, queries):
    answer = []
    array = dict()
    reversed_array = dict()

    # 글자 길이로 저장
    for word in words:
        n = len(word)
        if n in array.keys():
            array[n].append(word)
        else:
            array[n] = [word]

        word = word[::-1]
        if n in reversed_array.keys():
            reversed_array[n].append(word)
        else:
            reversed_array[n] = [word]

    # 오름차순 정렬
    for key, value in array.items():
        array[key] = sorted(value)

    for key, value in reversed_array.items():
        reversed_array[key] = sorted(value)

    # 이진탐색
    for query in queries:
        length = len(query)

        # 길이 있나 확인
        if length not in array.keys():
            answer.append(0)
            continue

        if query[0] == '?':  # 접두사 ?
            result = count_by_range(reversed_array[length], query[::-1].replace('?', 'a'), query[::-1].replace('?', 'z'))
        else:  # 접미사 ?
            result = count_by_range(array[length], query.replace('?', 'a'), query.replace('?', 'z'))

        answer.append(result)

    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?", "?????"]))











