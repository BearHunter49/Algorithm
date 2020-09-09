N = int(input())  # 1 <= N <= 1000

dp = [False] * 1001  # 인덱스 0 빼기
# 초기값
dp[1] = True

for i in range(2, 1001):

    if i % 5 == 0:
        test = i // 5
        if dp[test] == False:  # 5로 나눈 값이 못생긴 수가 아님
            dp[i] = False
        else:  # 못생긴 수
            dp[i] = True

    elif i % 3 == 0:
        test = i // 3
        if dp[test] == False:  # 3으로 나눈 값이 못생긴 수가 아님
            dp[i] = False
        else:  # 못생긴 수
            dp[i] = True

    elif i % 2 == 0:
        test = i // 2
        if dp[test] == False:  # 2으로 나눈 값이 못생긴 수가 아님
            dp[i] = False
        else:  # 못생긴 수
            dp[i] = True

for i in range(1, 1001):
    if dp[i] == True:
        N -= 1

    if N == 0:
        print(i)
        break

# N의 최대 범위가 작을 때 사용











