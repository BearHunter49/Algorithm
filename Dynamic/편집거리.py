A = input()
B = input()

A_len = len(A)
B_len = len(B)

dp = [[0] * (B_len + 1) for _ in range(A_len + 1)]  # 인덱스 0 넣기

# 초기값
for i in range(B_len + 1):
    dp[0][i] = i
for i in range(A_len + 1):
    dp[i][0] = i

# 편집 거리 알고리즘
for i in range(1, A_len + 1):
    for j in range(1, B_len + 1):

        # 두 문자가 같은 경우
        if A[i - 1] == B[j - 1]:
            dp[i][j] = dp[i - 1][j - 1]  # 전 문자까지의 변환 그대로

        # 두 문자가 다른 경우
        else:
            # 왼쪽, 왼쪽 위, 위쪽
            dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1

print(dp[-1][-1])

# 외우기!!





