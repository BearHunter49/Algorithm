from itertools import combinations

N, M = map(int, input().split())  # N: 도시 크기, M: 남겨야 하는 치킨 집 개수

city = list()
for _ in range(N):
    city.append(list(map(int, input().split())))

chicken_locations = list()  # 치킨 집 좌표
house_locations = list()  # 집 좌표
for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            chicken_locations.append((i, j))  # 치킨 집 좌표 저장
        elif city[i][j] == 1:
            house_locations.append((i, j))

# 알고리즘
result = int(1e9)  # 가장 작은 치킨 거리 합
for comb in combinations(chicken_locations, M):  # 모든 치킨 집 조합 살펴보기

    total_distance = 0  # 모든 집의 치킨 거리 합
    for house_x, house_y in house_locations:  # 각 집 좌표

        min_distance = int(1e9)  # 현재 집과 가장 가까운 치킨 거리
        for chicken_x, chicken_y in comb:  # 각 치킨 집 좌표

            distance = abs(house_x - chicken_x) + abs(house_y - chicken_y)
            min_distance = min(min_distance, distance)

        total_distance += min_distance

    result = min(result, total_distance)

print(result)










