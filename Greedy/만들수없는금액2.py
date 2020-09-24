N = int(input())  # 동전 개수
coins = list(map(int, input().split()))  # 동전들

coins.sort()  # 오름차순 정렬
result = 0
if coins[0] != 1:  # 1원 못만듬
    print(1)
else:
    possible = 1
    for i in range(1, N):
        if coins[i] <= possible + 1:  # 가능한 금액의 다음보다 같거나 작으면 모든 조건 충족 가능
            possible += coins[i]
        else:  # 가능한 금액보다 크면
            result = possible + 1

    print(result)







