N = int(input())
storage_list = list(map(int, input().split()))

dp_list = [0] * N

dp_list[0] = storage_list[0]
dp_list[1] = max(storage_list[0], storage_list[1])

for i in range(2, N):
    dp_list[i] = max(dp_list[i - 2] + storage_list[i], dp_list[i - 1])

print(dp_list[-1])




