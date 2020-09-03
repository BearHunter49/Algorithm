from itertools import combinations

N, M = map(int, input().split())  # N: 볼링공 개수, M: 공의 최대 무게
balls = list(map(int, input().split()))  # 볼링공 무개 리스트, 인덱스가 번호

possible_list = list(combinations(balls, 2))  # 가능한 모든 공 조합

result = len(possible_list)  # 총 조합 수
for comb in possible_list:
    if comb[0] == comb[1]:  # 무게가 같으면
        result -= 1

print(result)




