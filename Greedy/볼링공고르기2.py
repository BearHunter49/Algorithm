from itertools import combinations

N, M = map(int, input().split())  # N: 볼링공 개수, M: 공 최대 무게
balls = list(map(int, input().split()))

possible_list = list(combinations(balls, 2))
total = len(possible_list)
for possible in possible_list:
    if possible[0] == possible[1]:
        total -= 1

print(total)






