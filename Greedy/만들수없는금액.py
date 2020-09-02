N = int(input())
coin_list = list(map(int, input().split()))

coin_list.sort(reverse=True)  # 내림차순

result = 0
for i in range(1, sum(coin_list)):
    won = i
    for coin in coin_list:
        if coin <= won:
            won -= coin

    if won != 0:
        result = i
        break

print(result)




