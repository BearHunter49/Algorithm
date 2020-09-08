import heapq

N = int(input())  # 카드 뭉치 개수

heap = list()
for _ in range(N):  # 최소힙 만들기
    heapq.heappush(heap, int(input()))

total = 0

while True:  # 다 빌 때 까지
    first = heapq.heappop(heap)  # 가장 작은
    if not heap:  # 비었으면
        break
    second = heapq.heappop(heap)  # 그 다음 작은

    two_sum = first + second
    heapq.heappush(heap, two_sum)  # 다시 힙에 넣기

    total += two_sum

print(total)









