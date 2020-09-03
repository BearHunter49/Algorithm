N, M = map(int, input().split())  # N: 볼링공 개수, M: 공의 최대 무게
balls = list(map(int, input().split()))  # 볼링공 무개 리스트, 인덱스가 번호

# Counting 하기
count_of_weight = [0] * 11  # 무게는 10 까지만 있음
for ball in balls:
    count_of_weight[ball] += 1

result = 0

# 무게 별 계산
for i in range(1, 11):
    N -= count_of_weight[i]  # 나머지 공 개수 업데이트
    result += count_of_weight[i] * N  # 현재 무게의 공 개수 x 나머지 무게 공 개수

print(result)






