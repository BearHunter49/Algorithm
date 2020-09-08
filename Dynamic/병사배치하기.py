N = int(input())  # 병사 수
soldier_list = list(map(int, input().split()))

dp = [1] * N  # 내림차순 병사 개수
for i in range(1, N):  # 현재 병사
    for j in range(0, i):  # 앞쪽 병사
        if soldier_list[j] > soldier_list[i]:  # 앞쪽에 자기보다 큰 병사들
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))













