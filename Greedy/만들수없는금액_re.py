N = int(input())
coin_list = list(map(int, input().split()))

coin_list.sort()  # 오름차순

target = 1
for coin in coin_list:
    if target < coin:
        break
    target += coin

print(target)











