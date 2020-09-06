N = int(input())  # 집 개수
houses = list(map(int, input().split()))
houses.sort()  # 오름차순 정렬

print(houses[(N - 1) // 2])













