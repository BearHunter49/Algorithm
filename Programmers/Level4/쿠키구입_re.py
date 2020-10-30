def solution(cookie):
    answer = 0
    n = len(cookie)

    for i in range(n - 1):
        left, left_index = cookie[i], i
        right, right_index = cookie[i + 1], i + 1
        while True:
            if left == right:
                answer = max(answer, left)
            if left >= right and right_index + 1 < n:
                right_index += 1
                right += cookie[right_index]
                continue
            if left < right and left_index - 1 >= 0:
                left_index -= 1
                left += cookie[left_index]
                continue
            break

    return answer


print(solution([4,3,5,2,6,8]))
