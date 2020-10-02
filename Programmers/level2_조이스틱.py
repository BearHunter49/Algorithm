alphabet_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                 "U", "V", "W", "X", "Y", "Z"]


def find_next_position(name, current_position, checked):
    length = len(checked)
    is_finished = True

    # 작명 시작일 때
    if not checked[current_position]:
        return current_position, 0

    # 오른쪽으로 찾기
    right_distance = 0
    right_search = 0
    for i in range(1, length):
        right_search = (current_position + i) % length
        right_distance = i
        if not checked[right_search] and name[right_search] != "A":  # 체크 안한 곳 (A도 아님)
            is_finished = False
            break

    # 왼쪽으로 찾기
    left_distance = 0
    left_search = 0
    for i in range(1, length):
        left_search = (current_position - i) % length
        left_distance = i
        if not checked[left_search] and name[left_search] != "A":  # 체크 안한 곳 (A도 아님)
            is_finished = False
            break

    if is_finished:  # 끝났으면
        return -1, 0

    # 더 가까운 쪽 선택
    if right_distance > left_distance:
        return left_search, left_distance
    else:
        return right_search, right_distance


def solution(name):
    answer = 0

    length = len(name)
    checked = [False] * length

    current_position = 0
    while True:
        next_position, distance = find_next_position(name, current_position, checked)

        if next_position == -1:  # 끝났으면
            break

        answer += distance  # 자릿수 이동 비용

        # 알파벳 바꾸는 비용
        target_alphabet = alphabet_list.index(name[next_position])
        a_to = target_alphabet
        z_to = 26 - target_alphabet
        if a_to < z_to:  # A부터 가는게 빠름
            answer += a_to
        else:  # Z부터 가는게 빠름
            answer += z_to

        current_position = next_position
        checked[current_position] = True

    return answer


print(solution("ACAAA"))