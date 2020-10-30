max_sum = 0


def has_same_part(prefix_sum, x, y):
    global max_sum

    for m in range(x, y):
        until_l = 0
        if x - 1 >= 0:
            until_l = prefix_sum[x - 1]
        left = prefix_sum[m] - until_l
        right = prefix_sum[y] - prefix_sum[m]

        if left == right:
            max_sum = max(max_sum, left)


def solution(cookie):
    global max_sum

    n = len(cookie)
    prefix_sum = [0] * n
    prefix_sum[0] = cookie[0]
    for i in range(1, n):
        prefix_sum[i] = cookie[i] + prefix_sum[i - 1]

    for i in range(n - 1):
        for j in range(i + 1, n):
            has_same_part(prefix_sum, i, j)

    return max_sum


print(solution([4,3,5,2,6,8]))
