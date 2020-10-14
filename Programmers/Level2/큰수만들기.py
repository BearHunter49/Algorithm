import copy


def solution(number, k):
    answer = ''

    new_number = [(int(num), i) for i, num in enumerate(number)]
    new_number.sort(key=lambda x: (-x[0], x[1]))  # (숫자, 인덱스)

    start_index = 0
    while True:
        if k == 0:  # 다 제거함
            answer += number
            break

        elif not number:  # k는 있는데 끝남
            answer = answer[:-k]
            break

        # 최댓값 index 찾기
        max_index = 0
        for num, index in new_number:
            if 0 <= index - start_index <= k:
                max_index = index - start_index
                break

        # 제거
        number = number[max_index:]
        k -= max_index

        # answer 추가
        answer += str(number[0])
        number = number[1:]

        start_index = start_index + max_index + 1

    return answer


print(solution("4177252841", 4))

