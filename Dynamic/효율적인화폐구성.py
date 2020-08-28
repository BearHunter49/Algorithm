N, M = map(int, input().split())
money_list = [int(input()) for _ in range(N)]

dp_list = [10001] * (M + 1)
for money in money_list:
    dp_list[money] = 1

for i in range(M + 1):

    # 규칙
    for money in money_list:
        if i - money >= 0:  # 안전 할때만
            dp_list[i] = min(dp_list[i], dp_list[i - money] + 1)

if dp_list[M] == 10001:
    print(-1)
else:
    print(dp_list[M])


