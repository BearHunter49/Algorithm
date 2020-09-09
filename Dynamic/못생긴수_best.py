N = int(input())  # 1 <= N <= 1000

dp = [0] * N
dp[0] = 1  # 못생긴 수 1이 시작

i2 = i3 = i5 = 0  # 들여보는 인덱스
next2, next3, next5 = 2, 3, 5  # 시작값: 1 * 2, 1 * 3, 1 * 5 값들

for i in range(1, N):
    dp[i] = min(next2, next3, next5)  # 가장 작은 다음 값

    if dp[i] == next2:
        i2 += 1
        next2 = dp[i2] * 2

    if dp[i] == next3:
        i3 += 1
        next3 = dp[i3] * 2

    if dp[i] == next5:
        i5 += 1
        next5 = dp[i5] * 2

print(dp[N - 1])

# N번만 돌면 됨. N의 범위가 10억개 등의 경우 효율적.









