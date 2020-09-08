N = int(input())  # 근무할 날짜
work_list = list()
work_list.append((0, 0))  # 인덱스 0 빼기
for _ in range(N):
    T, P = map(int, input().split())
    work_list.append((T, P))  # (걸리는 날짜, 받는 금액)

dp = [0] * (N + 1)  # 인덱스 0 빼기

max_value = 0  # 여태까지의 최대값
for i in range(N, 0, -1):
    T, P = work_list[i]

    if T + i <= N:  # 일 했을 때 날짜 안 넘어가면
        dp[i] = max(P + dp[T + i], max_value)  # (현재 날짜부터 한 금액 + 그 이후까지 한 금액) 과 현재 이후로의 최대 값
        max_value = dp[i]

    else:  # 넘어가면
        dp[i] = max_value

print(max_value)

# 뒤에서부터 함



