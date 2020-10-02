def solution(n):
    ans = 0

    while n != 0:
        q, r = divmod(n, 2)

        if r != 0:  # 2의 배수가 아니면 1칸 뛰기
            ans += 1
        n = q

    return ans


print(solution(5000))





