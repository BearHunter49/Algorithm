N, C = map(int, input().split())

houses = list()
for _ in range(N):
    houses.append(int(input()))

houses.sort()  # 오름차순 정렬

# 맨 첫번째는 무조건 설치
start = houses[1] - houses[0]  # 첫 집과 최소 거리
end = houses[-1] - houses[0]  # 첫 집과 최대 거리
result = 0

while start <= end:
    mid = (start + end) // 2  # 이번 간격
    count = 1  # 설치한 안테나 개수

    now_house = houses[0]
    for i in range(1, N):
        if houses[i] < now_house + mid:  # 최소거리 충족 안되면 설치 못함
            continue
        else:  # 설치 가능
            count += 1
            now_house = houses[i]

    if count >= C:  # C개 이상으로 설치했으면
        result = mid  # 저장
        start = mid + 1  # 거리 좀 더 늘려보기
    else:  # C개 설치 못 했으면
        end = mid - 1  # 거리 좀 더 줄여보기

print(result)
# 사이의 거리로 이진탐색




