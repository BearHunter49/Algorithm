def solution(n):
    answer = 0

    numbers = [i for i in range(n + 1)]  # 인덱스 0 빼고

    total = 0
    right_index = 0
    for left_index in range(1, n + 1):

        # 넓히기
        while total < n and right_index < n + 1:
            total += numbers[right_index]
            right_index += 1

        if total == n:  # 찾음
            answer += 1

        # 줄이기
        total -= numbers[left_index]

    return answer


print(solution(15))  # 4

