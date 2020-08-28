N, M = map(int, input().split())
money_list = [int(input()) for _ in range(N)]

dp_list = [10001] * (M + 1)
dp_list[0] = 0

for money in money_list:
    for i in range(money, M + 1):
        dp_list[i] = min(dp_list[i], dp_list[i - money] + 1)

if dp_list[M] == 10001:
    print(-1)
else:
    print(dp_list[M])


