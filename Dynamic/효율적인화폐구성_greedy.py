N, M = map(int, input().split())
money_list = [int(input()) for _ in range(N)]

money_list.sort(reverse=True)

count = 0
for money in money_list:
    q, M = divmod(M, money)
    count += q
    if M == 0:
        print(count)
        break

if M != 0:
    print(-1)

# 그리디로는 풀 수 없다!!!! (가장 작은 돈의 배수가 안 돼서)




