N = int(input())

dp_list = [0] * (N + 1)
dp_list[1] = 1
dp_list[2] = 3

for i in range(3, N + 1):
    dp_list[i] = dp_list[i - 1] + (dp_list[i - 2] * 2) % 796796

print(dp_list[N])

