N = int(input())
storage_list = list(map(int, input().split()))

dp_list = [0] * N

# 2개 까지는 그대로
dp_list[0] = storage_list[0]
dp_list[1] = storage_list[1]

for i in range(2, N):
    dp_list[i] = storage_list[i] + max(dp_list[:i - 1])

print(max(dp_list))




