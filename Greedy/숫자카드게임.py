N, M = map(int, input().split())
matrix = list()
for _ in range(N):
    matrix.append(list(map(int, input().split())))

min_list = list()
for row in matrix:
    min_list.append(min(row))

print(max(min_list))


